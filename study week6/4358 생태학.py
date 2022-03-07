import sys

trees = {}
all_trees = 0

while True:
    read = sys.stdin.readline()
    if read =='\n':
        break

    tree = read
    all_trees += 1

    if tree in trees:
        trees[tree] += 1
    else:
        trees[tree] = 1


sorted_trees = sorted(trees.items())

for key, value in sorted_trees:
    per = round((value/all_trees)*100, 4)
    print(key, '%.4f' %per)