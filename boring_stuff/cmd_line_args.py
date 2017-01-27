import sys

args = sys.argv

for i, arg in enumerate(args):
    if i >0:
        print ("arg[%d]= %s" %(i, arg))

