from operator import add

a = [1, 2, 3, 4, 5]
map(add, a[1:], a[:-1])

