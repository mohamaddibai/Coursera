#!/usr/bin/env python3
import sys
import subprocess

def replace_jane(lines):
   v = lines
   with open(v, mode='r') as file: 
       for line in file.readlines():
            xline =line.strip()
            print(xline)
            newline = xline.replace("jane", "jdoe")
            print(newline)
            subprocess.run(["mv", "-i", xline, newline])

if __name__ == '__main__':
    line = sys.argv[1]
    replace_jane(line)
        