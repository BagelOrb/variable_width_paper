#!/usr/bin/python

import sys
from parse import *

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

filename = sys.argv[1]
scale = float(sys.argv[2])

outfile = sys.argv[3]


with open(filename, 'r') as f:
  with open(outfile, 'w') as out:
    for line in f:
      result = parse("G5 X{} Y{} {}", line)
      if result != None:
        (x, y, rest) = result
        out.write("G5 X" + str(float(x) * scale) + " Y" + str(float(y) * scale) + " " + rest + "\n")
      else:
        out.write(line)
