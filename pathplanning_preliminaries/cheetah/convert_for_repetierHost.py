#!/usr/bin/python

import sys
from parse import *
from math import *

#print('Number of arguments:', len(sys.argv), 'arguments.')
#print('Argument List:', str(sys.argv))

filename = sys.argv[1]
outfile = sys.argv[2]

last_x = 0
last_y = 0
with open(filename, 'r') as f:
  with open(outfile, 'w') as out:
    for (line_nr, line) in enumerate(f):
      if line.startswith("M82"):
        out.write("M83 ; relative extrusion mode")
        continue
      result = parse("G5 X{} Y{} S{} E{}", line)
      if result != None:
        (_x, _y, s, e) = result
        x = float(_x)
        y = float(_y)
        dist = sqrt((x - last_x)**2 + (y - last_y)**2)
        w = float(s) *0+1* float(e)
        ee = w * dist
        print(w, dist, ee)
        #print(str(line_nr) + " : " + x + " ; " + y + " ; " + s + " ; " + e)
        out.write("G1 X" + _x + " Y" + _y + " E" + str(w) + "\n")
        last_x = x
        last_y = y
      else:
        out.write(line)
