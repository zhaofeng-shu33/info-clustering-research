# Makefile for thucoursework

BUILD_DIR = ./build

.PHONY: all

all: $(BUILD_DIR)/main.pdf $(BUILD_DIR)/clustering.pdf

compare.tex:
	wget https://programmierung.oss-cn-shenzhen.aliyuncs.com/research/info-clustering/code/utility/compare.tex

$(BUILD_DIR)/main.pdf: compare.tex main.tex
	# run twice to generate the toc and make label and reference work
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) main.tex
	xelatex -output-directory=$(BUILD_DIR) main.tex

$(BUILD_DIR)/clustering.pdf: compare.tex clustering.tex
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) clustering.tex
	xelatex -output-directory=$(BUILD_DIR) clustering.tex

