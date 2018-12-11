# Makefile for thucoursework

# Compiling method: xelatex/pdflatex
INSTALL_PACKAGE = install-tl-unx.tar.gz
# if installation dir is changed, corresponding tl.profile should also be changed.
INSTALLER_DIR = /tmp/installer-texlive
# automatic configuration of mirror
REMOTE_INSTALLER_URL = http://mirror.ctan.org/systems/texlive/tlnet
# Set opts for latexmk if you use it
LATEXMKOPTS = -xelatex -halt-on-error -interaction=nonstopmode
BUILD_DIR = ./build

.PHONY: all pre_install_dep install_dep after_install_dep after_install_dep_2 clean

all: after_install_dep_2 main.pdf

pre_install_dep: $(INSTALL_PACKAGE)

after_install_dep_2: /tmp/texlive/texmf.cnf
	ls /tmp/texlive
	$(eval PLATFORM1=`$(INSTALLER_DIR)/install-tl --print-platform`)
	$(eval PLATFORM2=$(shell echo $(PLATFORM1)))
	$(eval PLATFORM3=$(shell pwd))
	$(eval export PATH :=$(PLATFORM3)/texlive/bin/$(PLATFORM2):$(PATH))
	echo $$PATH	
	
/tmp/texlive/texmf.cnf: after_install_dep
after_install_dep: install_dep
	# use tlmgr to install individual package
	tlmgr install beamer etoolbox translator caption mathtools
install_dep: pre_install_dep
	mkdir -p $(INSTALLER_DIR)
	tar -zxvf $(INSTALL_PACKAGE) -C $(INSTALLER_DIR) --strip-components 1 
	$(INSTALLER_DIR)/install-tl -profile tl.profile

$(INSTALL_PACKAGE): 
	wget $(REMOTE_INSTALLER_URL)/$(INSTALL_PACKAGE)

clean: 
	rm -fr $(INSTALLER_DIR)
	rm -f *.idx *.ilg *.glo *.gls *.hd *.ind *.log *.out *.synctex.gz *.toc *.aux

main.pdf: main.tex
	# run twice to generate the toc and make label and reference work
	mkdir -p $(BUILD_DIR)
	xelatex -output-directory=$(BUILD_DIR) main.tex
	xelatex -output-directory=$(BUILD_DIR) main.tex



