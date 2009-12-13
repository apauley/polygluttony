import sys
filename = sys.argv[0]
f = file(filename, 'r')
print f.read(),
f.close()
