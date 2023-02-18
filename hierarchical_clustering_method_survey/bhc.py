"""
Copyright (C) 2015 Baxter Eaves
License: Do what the fuck you want to public license (WTFPL) V2

Bayesian hierarchical clustering.

Heller, K. A., & Ghahramani, Z. (2005). Bayesian Hierarchical Clustering.
    Neuroscience, 6(section 2), 297鈥?04. doi:10.1145/1102351.1102389
"""
import itertools as it
import numpy as np

from scipy.special import multigammaln
from numpy.linalg import slogdet
from numpy import logaddexp
from math import pi
from math import log
from math import exp
from math import expm1
from math import lgamma
from scipy.cluster.hierarchy import dendrogram, fcluster

LOGPI = log(pi)
LOG2 = log(2)

def bhc_predict(data, data_model):
    """
    Compute Posterior p(x|D) distribution 
    """
def bhc(data, data_model, crp_alpha=1.0):
    """
    Bayesian hierarchical clustering CRP mixture model.

    Notes
    -----
    The Dirichlet process version of BHC suffers from terrible numerical
    errors when there are too many data points. 60 is about the limit. One
    could use arbitrary-precision numbers if one were so inclined.

    Parameters
    ----------
    data : numpy.ndarray (n, d)
        Array of data where each row is a data point and each column is a
        dimension.
    data_model : CollapsibleDistribution
        Provides the approprite ``log_marginal_likelihood`` function for the
        data.
    crp_alpha : float (0, Inf)
        CRP concentration parameter.

    Returns
    -------
    linkage_matrix : The hierarchical clustering encoded as a linkage matrix.
    """
    # initialize the tree
    nodes = dict((i, Node(np.array([x]), data_model, i, crp_alpha))
                 for i, x in enumerate(data))
    n_nodes = len(nodes)
    linkage_matrix = []
    lmls = []
    merged_node_index = n_nodes
    while n_nodes > 1:
        max_rk = float('-Inf')
        merged_node = None

        # for each pair of clusters (nodes), compute the merger score.
        for left_idx, right_idx in it.combinations(nodes.keys(), 2):
            tmp_node = Node.as_merge(nodes[left_idx], nodes[right_idx])

            logp_left = nodes[left_idx].logp
            logp_right = nodes[right_idx].logp
            logp_comb = tmp_node.logp

            log_pi = tmp_node.log_pi

            numer = log_pi + logp_comb

            neg_pi = log(-expm1(log_pi))
            denom = logaddexp(numer, neg_pi+logp_left+logp_right)

            log_rk = numer-denom

            if log_rk > max_rk:
                max_rk = log_rk
                merged_node = tmp_node
                merged_right = right_idx
                merged_left = left_idx

        # Merge the highest-scoring pair
        merged_node.num_children = nodes[merged_left].num_children + nodes[merged_right].num_children
        merged_node.index = merged_node_index
        merged_left_index = nodes[merged_left].index
        merged_right_index = nodes[merged_right].index
        del nodes[merged_right]
        nodes[merged_left] = merged_node
        
        linkage_matrix.append([merged_left_index, merged_right_index, np.fabs(denom), merged_node.num_children])
        merged_node_index += 1
        n_nodes -= 1
    # The denominator of log_rk is at the final merge is an estimate of the
    # marginal likelihood of the data under DPMM
    # lml = denom
    return np.asarray(linkage_matrix)


class Node(object):
    """ A node in the hierarchical clustering.

    Attributes
    ----------
    nk : int
        Number of data points assigned to the node
    data : numpy.ndarrary (n, d)
        The data assigned to the Node. Each row is a datum.
    crp_alpha : float
        CRP concentration parameter
    log_dk : float
        Some kind of number for computing probabilities
    log_pi : float
        For to compute merge probability
    """

    def __init__(self, data, data_model, index, crp_alpha=1.0, log_dk=None,
                 log_pi=0.0):
        """
        Parameters
        ----------
        data : numpy.ndarray
            Array of data_model-appropriate data
        data_model : idsteach.CollapsibleDistribution
            For to calculate marginal likelihoods
        crp_alpha : float (0, Inf)
            CRP concentration parameter
        log_dk : float
            Cached probability variable. Do not define if the node is a leaf.
        log_pi : float
            Cached probability variable. Do not define if the node is a leaf.
        """
        self.data_model = data_model
        self.data = data
        self.nk = data.shape[0]
        self.crp_alpha = crp_alpha
        self.log_pi = log_pi
        self.num_children = 1
        self.index = index
        if log_dk is None:
            self.log_dk = log(crp_alpha)
        else:
            self.log_dk = log_dk

        self.logp = self.data_model.log_marginal_likelihood(self.data)

    @classmethod
    def as_merge(cls, node_left, node_right):
        """ Create a node from two other nodes

        Parameters
        ----------
        node_left : Node
            the Node on the left
        node_right : Node
            The Node on the right
        """
        crp_alpha = node_left.crp_alpha
        data_model = node_left.data_model
        data = np.vstack((node_left.data, node_right.data))

        nk = data.shape[0]
        log_dk = logaddexp(log(crp_alpha) + lgamma(nk),
                           node_left.log_dk + node_right.log_dk)
        log_pi = log(crp_alpha) + lgamma(nk) - log_dk

        if log_pi == 0:
            raise RuntimeError('Precision error')

        return cls(data, data_model, -1, crp_alpha, log_dk, log_pi)


class CollapsibleDistribution(object):
    """ Abstract base class for a family of conjugate distributions. """

    def log_marginal_likelihood(self, X):
        """ Log of the marginal likelihood, P(X|prior).  """
        pass


class NormalInverseWishart(CollapsibleDistribution):
    """
    Multivariate Normal likelihood with multivariate Normal prior on mean and
    Inverse-Wishart prior on the covariance matrix.

    All math taken from Kevin Murphy's 2007 technical report, 'Conjugate
    Bayesian analysis of the Gaussian distribution'.
    """

    def __init__(self, **prior_hyperparameters):
        self.nu_0 = prior_hyperparameters['nu_0']
        self.mu_0 = prior_hyperparameters['mu_0']
        self.lambda_0 = prior_hyperparameters['lambda_0']
        self.psi_0 = prior_hyperparameters['psi_0']

        self.d = float(len(self.mu_0))

        self.log_z = self.calc_log_z(self.mu_0, self.psi_0, self.lambda_0,
                                     self.nu_0)

    @staticmethod
    def update_parameters(X, _mu, _psi, _lambda, _nu, _d):
        n = X.shape[0]
        xbar = np.mean(X, axis=0)
        lambda_n = _lambda + n
        nu_n = _nu + n
        mu_n = (_lambda*_mu + n*xbar)/lambda_n

        S = np.zeros(_psi.shape) if n == 1 else (n-1)*np.cov(X.T)
        dt = (xbar-_mu)[np.newaxis]

        back = np.dot(dt.T, dt)
        psi_n = _psi + S + (_lambda*n/lambda_n)*back

        assert(mu_n.shape[0] == _mu.shape[0])
        assert(psi_n.shape[0] == _psi.shape[0])
        assert(psi_n.shape[1] == _psi.shape[1])

        return mu_n, psi_n, lambda_n, nu_n

    @staticmethod
    def calc_log_z(_mu, _psi, _lambda, _nu):
        d = len(_mu)
        sign, detr = slogdet(_psi)
        log_z = (d/2.0)*log(2*pi/_lambda) +\
            multigammaln(_nu/2, d) - (_nu/2.0)*detr

        return log_z

    def log_marginal_likelihood(self, X):
        n = X.shape[0]
        params_n = self.update_parameters(X, self.mu_0, self.psi_0,
                                          self.lambda_0, self.nu_0, self.d)
        log_z_n = self.calc_log_z(*params_n)

        return log_z_n - self.log_z - LOGPI*(n*self.d/2)

def makeLinkageMatrix(asgn,lmls):
    N = len(asgn[0])
    Z = np.zeros((N-1,4),dtype=np.double)
    parents=dict([(i,i) for i in range(N)])
    nleaves = dict([(i,1.0) for i in range(N)])
    for i in range(N-1):
        L0 = asgn[i]
        L1 = asgn[i+1]
        for j in range(N):
            if L0[j] != L1[j] and parents[L0[j]]!= parents[L1[j]]:
                Z[i,0] = parents[L0[j]]
                Z[i,1] = parents[L1[j]]

                Z[i,2] = np.fabs(lmls[i]) #-lmls[i+1] if i<N-2 else lmls[N-2]-lmls[N-3]
                Z[i,3] = np.double(nleaves[parents[L0[j]]] + nleaves[parents[L1[j]]])
                
                parents[L0[j]]= N+i
                parents[L1[j]]= N+i
                nleaves[N+i] = Z[i,3]
    print(Z)
    return Z
if __name__ == '__main__':
    import matplotlib.pyplot as plt

    n_per_cat = 2

    def gen_data(n_per_cat):
        cov = np.eye(2)*0.2
        X0 = np.random.multivariate_normal([-2.0, 0.0], cov, n_per_cat)
        X1 = np.random.multivariate_normal([2.0, 0.0], cov, n_per_cat)
        X2 = np.random.multivariate_normal([0.0, 1.8], cov, n_per_cat)

        data = np.vstack((X0, X1, X2))
        return data

    hypers = {
        'mu_0': np.zeros(2),
        'nu_0': 3.0,
        'lambda_0': 1.0,
        'psi_0': np.eye(2)
    }
    data_model = NormalInverseWishart(**hypers)

    # Sanity check: grab the assignment that has three components and do a
    # visual verification.
    data = gen_data(15)
    linkage_matrix = bhc(data, data_model)
    print(linkage_matrix)
    # print('len of lml',len(lmls),'len of data',len(asgn[0]))
    #　print(makeLinkageMatrix(asgn,lmls))
    dn = dendrogram(linkage_matrix)
    plt.show()
    z = fcluster(linkage_matrix, 3, 'maxclust')
    plt.figure(tight_layout=True, facecolor='white')
    plt.scatter(data[:, 0], data[:, 1], c=z, cmap='Set1', s=225)
    plt.show()
