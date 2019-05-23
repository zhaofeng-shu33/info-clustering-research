# How to build
```shell
mkdir build
cp exportlist.bib build/
xelatex -output-directory=build nips_2019.tex
cd build && bibtex nips_2019.aux
cd .. && xelatex -output-directory=build nips_2019.tex
xelatex -output-directory=build nips_2019.tex # rerun
```
## template style file
Download the template style file to the current directory first.
[neurips_2019.sty](https://media.neurips.cc/Conferences/NeurIPS2019/Styles/neurips_2019.sty)

## experiment table file
The experiment 1 table tex file is named as `compare_3.tex`. First you need to generate the 
table, see the subdirectory **experiment/data_clustering** for detail; then copy the generated file to current build directory.

```shell
mkdir -p build
cp ../experiment/data-clustering/build/compare_3.tex ./build/
```

If you cannot make the table file, you can download [compare_3.tex](https://programmierung.oss-cn-shenzhen.aliyuncs.com/research/info-clustering/code/utility/parameter.json) 
and put it in the build directory.