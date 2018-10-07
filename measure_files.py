#!/usr/bin/env python
'''
  write file counts of directories
'''

import argparse
import logging
import os
import sys

def main(directories, names, noheader):
  logging.info('starting...')

  if not noheader:
    sys.stdout.write('{}\n'.format('\t'.join(names)))

  result = []
  for name, directory in zip(names, directories):
    all_files = os.listdir(directory) # dir is your directory path
    result.append(len(all_files))
  sys.stdout.write('{}\n'.format('\t'.join([str(x) for x in result])))

  logging.info('done')

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Assess MSI')
  parser.add_argument('--directories', nargs='+', required=True, help='directory names')
  parser.add_argument('--names', nargs='+', required=True, help='column names')
  parser.add_argument('--noheader', action='store_true', help='do not add header')
  parser.add_argument('--verbose', action='store_true', help='more logging')
  args = parser.parse_args()
  if args.verbose:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.DEBUG)
  else:
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)

  main(args.directories, args.names, args.noheader)
