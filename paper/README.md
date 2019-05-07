# How to build

## template style file
Download the template style file to the current directory first.
[neurips_2019.sty](https://media.neurips.cc/Conferences/NeurIPS2019/Styles/neurips_2019.sty)

## experiment table file
The experiment 1 table tex file is named as `compare_3.tex`. First you need to generate the 
table, see [utility](https://github.com/zhaofeng-shu33/principal_sequence_of_partition/tree/master/utility) for detail; then copy the generated file to current build directory.

```shell
mkdir -p build
cp ../code/utility/build/compare_3.tex ./build/
```