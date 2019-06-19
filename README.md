[![Build Status](https://travis-ci.org/zhaofeng-shu33/info-clustering-research.svg?branch=master)](https://travis-ci.org/zhaofeng-shu33/info-clustering-research)
# Introduction
This project contains the in-progress research about info-clustering. 
It can be divided into three parts in general:

* research document, paper, presentation and poster
* experiment code and result
* [info-clustering](https://github.com/zhaofeng-shu33/principal_sequence_of_partition) implementation

## Research document
 * `main.tex` : presentation slides
 * `clustering.tex` : article.
 * paper in progress 

### Template 
The presentation uses a beamer template customized for TBSI Lab2C, which is based on `Madrid`, modified by [xiangxiang-xu](https://xiangxiangxu.com/)
and packaged by *zhaofeng-shu33*. If you want to use it in your beamer presentation, follows:
```latex
\documentclass{beamer}
\usetheme{Lab2C}
%other materials
```

## Experiment result

### Data Clustering
We did a simple comparision between 5 different clustering methods on 5 different datasets. 
The score table is called `compare.tex` and is an input to `main.tex`. If you don't want to run the experiment locally,
you can download [compare.tex](http://data-visualization.leidenschaft.cn/research/info-clustering/code/utility/compare.tex).
If you use linux os, you can use `Makefile` to handle the dependencies.

### Community Detection

