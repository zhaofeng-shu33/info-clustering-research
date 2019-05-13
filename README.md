[![Build Status](https://travis-ci.org/zhaofeng-shu33/lab2c_presentation_template.svg?branch=master)](https://travis-ci.org/zhaofeng-shu33/lab2c_presentation_template)
# Introduction
This project is document oriented and uses the result generated from the code project.
Actually, it uses the [code](https://github.com/zhaofeng-shu33/principal_sequence_of_partition) project as a submodule.

The document project provides `main.tex` and `clustering.tex`. The first is the presentation and the second is the article.

The presentation uses a beamer template customized for TBSI Lab2C, which is based on `Madrid`, modified by [xiangxiang-xu](https://xiangxiangxu.com/)
and packaged by *zhaofeng-shu33*. If you want to use it in your beamer presentation, follows:
```latex
\documentclass{beamer}
\usetheme{Lab2C}
%other materials
```
## Experiment result
We did a simple comparision between 5 different clustering methods on 5 different datasets. 
The experiment code is at [utility](https://github.com/zhaofeng-shu33/principal_sequence_of_partition/tree/master/utility).
The score table is called `compare.tex` and is an input to `main.tex`. If you don't want to run the experiment locally,
you can download [compare.tex](http://data-visualization.leidenschaft.cn/research/info-clustering/code/utility/compare.tex).
If you use linux os, you can use `Makefile` to handle the dependencies.

