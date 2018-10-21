#!/usr/bin/env python

import collections
from datetime import datetime
import sys

import matplotlib as mpl 
mpl.use('TkAgg') # osx
import matplotlib.pyplot as plt

def main():
  header = None
  xs = []
  ys = collections.defaultdict(list)
  top = 1

  for row in sys.stdin:
    fields = row.strip('\n').split('\t')
    if header is None:
      header = fields
      continue
    
    xs.append(datetime.strptime(fields[0], '%Y-%m-%d'))
    for idx in range(1, len(fields)):
      y = float(fields[idx])
      ys[header[idx]].append(y)
      top = max(y, top)

  plt.figure(figsize=(18,12))
  plt.ylim(bottom=0, top=top + 5)

  for idx in range(1, len(fields)):
    plt.plot(xs, ys[header[idx]], label=header[idx])

  plt.title('PhD Progress')
  plt.legend()
  plt.savefig(sys.argv[1])

if __name__ == '__main__':
  main()
