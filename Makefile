# Makefile for thucoursework

LATEXMKOPTS = -xelatex -halt-on-error -interaction=nonstopmode
BUILD_DIR = ./build

.PHONY: all

all: main.pdf

main.pdf: main.tex
	# run twice to generate the toc and make label and reference work
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) main.tex
	xelatex -output-directory=$(BUILD_DIR) main.tex



