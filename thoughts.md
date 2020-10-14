This part of research is centered on the algorithm.
That is, it uses PSP algorithm. It had good theoretical properties
and algorithmic implementations. However, the biggest problem is
that it performed poorly on large dataset. The hierarchical tree
generated is not regular even for some artificial dataset.
I guess the problem comes from the penalty term in the denominator
is linear with the number of partition, and as the graph size grows,
it became quite imbalanced. If we use |P|^2 term in the denominator,
it may produce good results if we can solve the optimization problem
exactly. However, the expression is quite sensitive and we have no idea
how to solve this problem when |P|^2 is used. When linear |P| is used,
the theory is based on submodular function minimization. For normalized
cut, the theory of spectral clustering can be used and this method
is practical in image segmentation.

Carefully fine-tuning the graph weight can improve the results of PSP
but the gain is not so large. The method of PSP is still inferior to
other popular methods in clustering or community detection. And we do
not think fine-tuning weight has much research value.

