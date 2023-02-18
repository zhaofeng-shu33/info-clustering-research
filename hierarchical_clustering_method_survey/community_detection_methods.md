## Modularity based method

Let $m$ be the number of edges, $A_{ij}$ be the adjacency matrix and $C_i$ be a cluster of the graph. The modularity is written as
$$
Q = \frac{1}{2m} \sum_{ij} (A_{ij} - P_{ij}) \delta(C_i, C_j)
$$
$P_{ij}$ represents the expected number of edges between vertices $i$ and $j$ in a random graph which has the same node degree distribution as the original graph. Suppose vertices $i$ and $j$ have degree $k_i$ and $k_j$ respectively, then $P_{ij} = \frac{k_i k_j}{2m}$.

Maximizing modularity gives a cluster of the graph.

Basic idea is to merge two clusters at each step. For sparse graph, Clauset et. al. [2004] proposes an efficient algorithm to accomplish this merge, which achieves $O(md\log n)$ where $d$ is the depth of the dendrogram. To achieve this time bound, $\Delta Q_{ij}$ is maintained rather than the adjacency matrix. See [fastmodularity](https://www.cs.unm.edu/~aaron/research/fastmodularity.htm) for detail.



## Divisive approach

The first algorithm in community detection is proposed by Newman and Girvan using a divisive approach. It removes one edge with the largest "betweenness" measure in each step until the graph is split into singletons. The betweenness measure is not unique. For example, we can use the shortest-path betweenness. That is, "the number of shortest paths between all vertex pairs that run along that edge". The time complexity to calculate this measure for all edges is $O(mn)$ using breadth first search for each node.

## Bayesian view

There is a method called BHCD [Blundell 2013], which is based on MAP. We try to find a tree structure such that the probability of the adjacency matrix $D$ is largest given this tree structure.  That is
$$
\max p(D | T)
$$
There is a recursive formula to compute $p(D|T)$ based on the consistent partition $\phi$.
$$
\begin{align}
\sigma^{\neg \textrm{ch}}_{SS} & = \sigma_{SS} - \sum_{C \in \textrm{ch}(S)} \sigma_{CC} \\
p(D_{TT} | T) &= \pi_T f(\sigma_{TT}) + (1-\pi_T) g(\sigma_{TT}^{\neg \textrm{ch}}) \prod_{C\in \textrm{ch}(T)} p(D_{CC} | C)
\end{align}
$$
We choose:
$$
\begin{align}
f(x,y) &= \frac{B(\alpha + x, \beta + y)}{B(\alpha, \beta)}, \alpha > \beta \\
g(x, y) &= \frac{B(\delta + x, \lambda + y)}{B(\delta, \lambda)}, \delta < \lambda \\
\sigma_{pq} & = (n^1_{pq}, n^0_{pq})
\end{align}
$$
$n^1_{pq}$ is the total number of edges between set $p$ and $q$ while $n^0_{pq}$ is the total number of observed absent edges between set $p$ and $q$.

In each iteration, a pair of tree $I$ and $J$ is to be merged to $M$ if they can increase $p(D|T)$ most:
$$
\textrm{SCORE}(M; I, J) = \frac{p(D_{MM} | F^*)}{p(D_{MM}|F)} = \frac{p(D_{MM}| M)}{p(D_{II} | I)p(D_{JJ}|J)g(\sigma_{IJ})}
$$


The forest $F$ results in forest $F^*$ in the merge.

Using efficient data structures (heap etc.), the time complexity of BHCD is controlled within $O(n^2 \log(n))$ for a graph with $n$ nodes. This is with the same time complexity of typical HAC. 