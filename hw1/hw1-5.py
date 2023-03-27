import sys

f = open(sys.argv[1], 'r')

data = f.read()
f.close()

f = open(sys.argv[2], 'w')
f.write(data)

f.close()