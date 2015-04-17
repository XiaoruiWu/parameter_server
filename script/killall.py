import os
import os.path
import sys
import subprocess

hostlist= sys.argv[1]

hosts = []
f = open(hostlist)
for line in f:
  cmd = './script/kill_node.sh %s' % line
  print cmd
  os.system(cmd)
f.close()
