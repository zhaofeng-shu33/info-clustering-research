# Makefile for thucoursework

# Compiling method: xelatex/pdflatex
INSTALL_PACKAGE = install-tl-unx.tar.gz
INSTALL_DIR = ./install-texlive
# automatic configuration of mirror
REMOTE_INSTALLER_URL = http://mirror.ctan.org/systems/texlive/tlnet
# Set opts for latexmk if you use it
LATEXMKOPTS = -xelatex -halt-on-error -interaction=nonstopmode
BUILD_DIR = ./build

.PHONY: all pre_install_dep install_dep after_install_dep clean

all: after_install_dep main.pdf

pre_install_dep: $(INSTALL_PACKAGE)

after_install_dep: install_dep
	# tricky, to make variable assignment in recipe, and to execute shell command and assign the print result to a variable.
	$(eval PLATFORM1=`$(INSTALL_DIR)/install-tl --print-platform`)
	$(eval PLATFORM2=$(shell echo $(PLATFORM1)))
	$(eval PLATFORM3=$(shell pwd))
	$(eval export PATH :=$(PLATFORM3)/texlive/bin/$(PLATFORM2):$(PATH))
	echo $$PATH	
	# to make tlmgr work, we need perl
	tlmgr install beamer etoolbox translator caption mathtools
install_dep: pre_install_dep
	mkdir -p $(INSTALL_DIR)
	tar -zxvf $(INSTALL_PACKAGE) -C $(INSTALL_DIR) --strip-components 1 
	$(INSTALL_DIR)/install-tl -profile tl.profile

$(INSTALL_PACKAGE): 
	wget $(REMOTE_INSTALLER_URL)/$(INSTALL_PACKAGE)

clean: 
	rm -fr $(INSTALL_DIR)
	rm -f *.idx *.ilg *.glo *.gls *.hd *.ind *.log *.out *.synctex.gz *.toc *.aux

main.pdf: main.tex
	# run twice to generate the toc and make label and reference work
	xelatex -output-directory=$(BUILD_DIR) main.tex
	xelatex -output-directory=$(BUILD_DIR) main.tex



