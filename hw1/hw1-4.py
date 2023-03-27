import sys

#print(sys.argv)

del sys.argv[0]

for arg in sys.argv:
    print(arg.upper(), end=" ")

print()