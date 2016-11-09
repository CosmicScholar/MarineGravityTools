import os


data=2000.08700533
command='gmt mgd77info 01010221 -E >info.dat'
os.system(command)
command='gmt mgd77list 01010221  -Da1982-08-14T01:09:00 -Fdist,azim,faa,depth  >output.dat'
os.system(command)