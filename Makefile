
BUILD_DIR = ./build

.PHONY: all

all: $(BUILD_DIR)/exportlist.bib $(BUILD_DIR)/main.pdf $(BUILD_DIR)/clustering.pdf ${BUILD_DIR}/psp_improved.pdf ${BUILD_DIR}/pmf.pdf $(BUILD_DIR)/trival_solution.pdf

$(BUILD_DIR)/exportlist.bib: exportlist.bib
	mkdir -p $(BUILD_DIR)
	cp exportlist.bib $(BUILD_DIR)/
	
$(BUILD_DIR)/main.pdf: main.tex
	# run twice to generate the toc and make label and reference work
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) main.tex
	xelatex -output-directory=$(BUILD_DIR) main.tex

$(BUILD_DIR)/clustering.pdf: clustering.tex
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) clustering.tex
	cd $(BUILD_DIR) && bibtex clustering.aux && cd ..
	xelatex -output-directory=$(BUILD_DIR) clustering.tex
	xelatex -output-directory=$(BUILD_DIR) clustering.tex

$(BUILD_DIR)/pmf.pdf: pmf.tex
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) pmf.tex
	xelatex -output-directory=$(BUILD_DIR) pmf.tex
	
$(BUILD_DIR)/psp_improved.pdf: psp_improved.tex
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) psp_improved.tex
	xelatex -output-directory=$(BUILD_DIR) psp_improved.tex

$(BUILD_DIR)/trival_solution.pdf: trivial_solution.tex
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) trivial_solution.tex    
	cd $(BUILD_DIR) && bibtex trival_solution.aux && cd ..    
	xelatex -output-directory=$(BUILD_DIR) trivial_solution.tex
	xelatex -output-directory=$(BUILD_DIR) trivial_solution.tex
