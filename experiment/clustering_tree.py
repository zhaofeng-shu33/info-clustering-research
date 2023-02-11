import numpy as np
from info_cluster import InfoCluster
from ete3 import TreeStyle

ic = InfoCluster(affinity='precomputed')
X=np.load('X.npy')
gamma = 0.5
ic.fit(np.exp(gamma * X))
columns = ['arb', 'asm', 'ben', 'brx', 'bul', 'cat', 'ces', 'cmn', 'dan', 'deu', 'ell', 'eng', 'epo', 'eus', 'fin', 'fra', 'glg', 'guj', 'heb', 
'hin', 'hrv', 'hun', 'ind', 'isl', 'ita', 'jpn', 'kan', 'kok', 'kor', 'lat', 'lit', 'mal', 'mon', 'msa', 'nep', 'nld', 'nob', 'ori', 'pan', 'pol', 'por', 'ron', 'rus', 'san', 'slk', 'slv', 'spa', 'sqi', 'swe', 'tam', 'tel', 'tha', 'tsn', 'tur', 'ukr', 'urd', 'vie', 'zsm', 'gla', 'gle', 'hye', 'kas', 'kat', 'mkd', 'nno', 'nso', 'zul']
new_columns = ['阿拉伯语', '阿萨姆语', '孟加拉语', 'brx', 'bul',
'加泰罗尼亚语', 'ces', '现代汉语', '丹麦语', '德语', '现代希腊语',
'英语', 'epo', '巴斯克语', '芬兰语',
'法语', '加利西亚语', 'guj', 'heb', 
'印地语', 'hrv', 'hun', '印度尼西亚语', 'isl', '意大利语',
'日语', '坎纳达语', 'kok', '韩语', '拉丁语', '立陶宛语', '马拉雅拉姆语', '蒙古语',
'马来语', 'nep', 'nld', 'nob', 'ori', 'pan', '波兰语', '葡萄牙语', '罗马尼亚语',
'俄语',
'san', 'slk', '斯洛文尼亚语', '西班牙语', 'sqi', '瑞典语',
'tam', 'tel', '泰语', 'tsn', '土尔其语', '乌克兰语', '乌尔都语', '越南语',
'zsm', '苏格兰盖尔语', '爱尔兰语', 'hye', 'kas', 'kat',
'mkd', 'nno', 'nso', 'zul']
for _n in ic.tree.traverse("postorder"):
    if _n.is_leaf():
        _n.name = new_columns[int(_n.name)]
print(ic.tree)
ic.tree.render('build/language_tree.pdf')
# ic.tree.render('build/language_tree.pdf')
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
