import numpy as np
from info_cluster import InfoCluster
from ete3 import TreeStyle

ic = InfoCluster(affinity='precomputed')
X=np.load('X.npy')
gamma = 0.5
ic.fit(np.exp(gamma * X))
columns = ['arb', 'asm', 'ben', 'brx', 'bul', 'cat',
'ces', 'cmn', 'dan', 'deu', 'ell', 'eng', 'epo', 'eus',
'fin', 'fra', 'glg', 'guj', 'heb', 'hin', 'hrv', 'hun',
'ind', 'isl', 'ita', 'jpn', 'kan', 'kok', 'kor', 'lat', 'lit',
'mal',
'mon', 'nep', 'nld', 'nob', 'ori', 'pan', 'pol', 'por', 'ron', 'rus', 'san', 'slk', 'slv', 'spa', 'sqi', 'swe', 'tam', 'tel', 'tha', 'tsn', 'tur', 'ukr', 'urd', 'vie', 'zsm', 'gla', 'gle', 'hye', 'kas', 'kat', 'mkd', 'nno', 'nso', 'zul']
new_columns = ['阿拉伯语', '阿萨姆语', '孟加拉语', '博多语', '保加利亚语',
'加泰罗尼亚语', '捷克语', '现代汉语', '丹麦语', '德语', '现代希腊语',
'英语', '世界语', '巴斯克语', '芬兰语',
'法语', '加利西亚语', '古吉拉特语', '希伯来语', 
'印地语', '克罗地亚语', '匈牙利语', '印度尼西亚语', '冰岛语', '意大利语',
'日语', '坎纳达语', '孔卡尼语', '韩语', '拉丁语', '立陶宛语',
'马拉雅拉姆语', '蒙古语',
'尼泊尔语', '荷兰语',
'书面挪威语', '奥里亚语', '旁遮普语', '波兰语', '葡萄牙语', '罗马尼亚语',
'俄语',
'梵语', '斯洛伐克语', '斯洛文尼亚语', '西班牙语', '阿尔巴尼亚语', '瑞典语',
'泰米尔语', '泰卢固语', '泰语', '茨瓦纳语',
'土尔其语', '乌克兰语', '乌尔都语', '越南语',
'马来语', '苏格兰盖尔语', '爱尔兰语', '亚美尼亚语', '克什米尔语', '格鲁吉亚语',
'马其顿语', '新挪威语', '北索托语', '祖鲁语']
for _n in ic.tree.traverse("postorder"):
    if _n.is_leaf():
        _n.name = new_columns[int(_n.name)]
print(ic.tree)
ts = TreeStyle()
# ts.rotation = 90
ts.show_scale = False

ic.tree.render('build/language_tree.pdf', tree_style=ts)
ic.tree.render('build/language_tree.png', tree_style=ts)
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
