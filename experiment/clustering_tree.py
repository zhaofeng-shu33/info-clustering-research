import numpy as np
from info_cluster import InfoCluster

ic = InfoCluster(affinity='precomputed')
X=np.load('X.npy')
gamma = 0.5
ic.fit(np.exp(gamma * X))
columns = ['arb', 'asm', 'ben', 'brx', 'bul', 'cat', 'ces', 'cmn', 'dan', 'deu', 'ell', 'eng', 'epo', 'eus', 'fin', 'fra', 'glg', 'guj', 'heb', 
'hin', 'hrv', 'hun', 'ind', 'isl', 'ita', 'jpn', 'kan', 'kok', 'kor', 'lat', 'lit', 'mal', 'mon', 'msa', 'nep', 'nld', 'nob', 'ori', 'pan', 'pol', 'por', 'ron', 'rus', 'san', 'slk', 'slv', 'spa', 'sqi', 'swe', 'tam', 'tel', 'tha', 'tsn', 'tur', 'ukr', 'urd', 'vie', 'zsm', 'gla', 'gle', 'hye', 'kas', 'kat', 'mkd', 'nno', 'nso', 'zul']
for _n in ic.tree.traverse("postorder"):
    if _n.is_leaf():
        _n.name = columns[int(_n.name)]
print(ic.tree)

#       /-arb
#      |
#      |                                                                                 /-asm
#      |                                                                                |
#      |                                                                              /-|--ben
#      |                                                                             |  |
#      |                                                                             |   \-ori
#      |                                                                           /-|
#      |                                                                          |  |      /-guj
#      |                                                                          |  |   /-|
#      |                                                                        /-|   \-|   \-nep
#      |                                                                       |  |     |
#      |                                                                       |  |      \-pan
#      |                                                                     /-|  |
#      |                                                                    |  |   \-kok
#      |                                                                  /-|  |
#      |                                                                 |  |   \-san
#      |                                                               /-|  |
#      |                                                              |  |   \-kan
#      |                                                            /-|  |
#      |                                                           |  |   \-mal
#      |                                                           |  |
#      |                                                           |   \-tel
#      |                                                           |
#      |                                                           |   /-bul
#      |                                                           |  |
#      |                                                           |  |      /-ces
#      |                                                           |  |   /-|
#      |                                                           |  |  |   \-slk
#      |                                                           |--|--|
#      |                                                           |  |  |   /-hrv
#      |                                                           |  |   \-|
#      |                                                           |  |      \-slv
#      |                                                           |  |
#      |                                                           |   \-mkd
#      |                                                           |
#      |                                                           |                     /-cat
#      |                                                           |                  /-|
#      |                                                           |               /-|   \-spa
#      |                                                           |              |  |
#      |                                                         /-|            /-|   \-glg
#      |                                                        |  |           |  |
#      |                                                        |  |         /-|   \-por
#      |                                                        |  |        |  |
#      |                                                        |  |      /-|   \-fra
#      |                                                        |  |     |  |
#      |                                                        |  |   /-|   \-ita
#      |                                                        |  |  |  |
#      |                                                        |  |--|   \-ron
#      |                                                        |  |  |
#      |                                                        |  |   \-eng
#      |                                                        |  |
#      |                                                      /-|  |      /-dan
#      |                                                     |  |  |   /-|
#      |                                                     |  |  |  |  |   /-nob
#      |                                                     |  |  |--|   \-|
#      |                                                     |  |  |  |      \-nno
#      |                                                     |  |  |  |
#      |                                                     |  |  |   \-swe
#      |                                                     |  |  |
#      |                                                     |  |  |--deu
#      |                                                   /-|  |  |
#      |                                                  |  |  |   \-nld
#      |                                                  |  |  |
#      |                                                  |  |   \-rus
#    /-|                                                  |  |
#   |  |                                                  |  |--epo
#   |  |                                                /-|  |
#   |  |                                               |  |  |--lat
#   |  |                                               |  |  |
#   |  |                                               |  |   \-ukr
#   |  |                                               |  |
#   |  |                                             /-|  |--urd
#   |  |                                            |  |  |
#   |  |                                            |  |   \-kas
#   |  |                                            |  |
#   |  |                                            |  |      /-ind
#   |  |                                          /-|  |   /-|
#   |  |                                         |  |   \-|   \-msa
#   |  |                                         |  |     |
#   |  |                                       /-|  |      \-zsm
#   |  |                                      |  |  |
#   |  |                                      |  |   \-eus
#   |  |                                    /-|  |
#   |  |                                   |  |   \-sqi
#   |  |                                 /-|  |
#   |  |                                |  |   \-brx
#   |  |                              /-|  |
#   |  |                             |  |   \-pol
#   |  |                           /-|  |
#   |  |                          |  |   \-lit
#   |  |                        /-|  |
#   |  |                       |  |   \-isl
#   |  |                       |  |
#   |  |                       |   \-hin
#   |  |                     /-|
#   |  |                    |  |--hun
#   |  |                    |  |
# --|  |                  /-|  |--gla
#   |  |                 |  |  |
#   |  |                 |  |   \-gle
#   |  |               /-|  |
#   |  |              |  |   \-tur
#   |  |            /-|  |
#   |  |           |  |   \-tam
#   |  |           |  |
#   |  |         /-|   \-fin
#   |  |        |  |
#   |  |        |  |--ell
#   |  |      /-|  |
#   |  |     |  |   \-kat
#   |  |   /-|  |
#   |  |  |  |   \-jpn
#   |  |  |  |
#   |  |--|   \-hye
#   |  |  |
#   |  |  |--tsn
#   |  |  |
#   |  |   \-nso
#   |  |
#   |  |--heb
#   |  |
#   |  |--kor
#   |  |
#   |  |--mon
#   |  |
#   |  |--tha
#   |  |
#   |  |--vie
#   |  |
#   |   \-zul
#   |
#    \-cmn