#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""
def get_special_paths(dir):
  filenames=os.listdir(dir[0])
  fullpath=[]
  for i in filenames[1:]:
    path=os.path.join(dir[0], i)
    fullpath.append(os.path.abspath(path))
  # print(fullpath)
  return fullpath

  # sys.exit()
  # for a in filenames[1:]:
  #   print(a)
  # sys.exit()
  # for x in dir:
  #   # filenames = os.listdir(x)
  #   print(x)
  # sys.exit()
  # for filename in filenames:
  #   path=os.path.join(dir, filename)
  #   os.path.abspath(path)
  #   return path

def copy_to(path,dir):
    # source = 'current/test/test.py' ## path to source file
    # target = path
    os.makedirs(path)
    fp=[]
    
    filenames=os.listdir(dir[0])[2:]
    for i in filenames:
      fp.append(path + "/" + i)
    # print(fp)
    # sys.exit()
    # print(get_special_paths(dir)[1:])
    # print(fp)
    # sys.exit()
    for i in range(len(get_special_paths(dir)[1:])):
      
      shutil.copy(get_special_paths(dir)[1:][i],fp[i])

# def zip_to(paths, zippath):

#   subprocess.call(, *, stdin=None, stdout=None, stderr=None, shell=False)
# +++your code here+++
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print("usage: [--todir dir][--tozip zipfile] dir [dir ...]");
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print("error: must specify one or more dirs")
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  get_special_paths(args)
  copy_to(todir,args)
if __name__ == "__main__":
  main()
