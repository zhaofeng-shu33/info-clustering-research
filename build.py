# build individual files
# 1. copy the source files to build dir
# 2. cd to build dir
# 3. write necessary headers
# 4. build the pdf files
import argparse
import os
from shutil import copyfile
BUILD_DIR = 'build'
MACRO = 'macros.tex'
HEADER = '\documentclass{article}\input{%s}\\begin{document}\input{%s}\end{document}'
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='input file')
    args = parser.parse_args()
    print('step 1: copying files')
    copyfile(args.file, os.path.join(BUILD_DIR, args.file))
    copyfile(MACRO, os.path.join(BUILD_DIR, MACRO))
    print('step 2: changing directory to ' + BUILD_DIR)
    root_dir = os.getcwd()
    os.chdir(BUILD_DIR)
    print('step 3: write necessary headers')
    output_file_name = args.file.replace('.','_r.')
    with open(output_file_name, 'w') as f:
        f.write(HEADER % (MACRO, args.file))
    print('step 4: build pdf files')
    os.system('xelatex -synctex=1 -include-directory=%s %s' % (root_dir, output_file_name))
        
    