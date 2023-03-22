n = int(input("n->"))
m = int(input("m->"))
set1 = set()
set2 = set()

for i in range(n):
    set1.add(int(input(f"{i}-> ")))

print("---")

for j in range(m):
    set2.add(int(input(f"{j}-> ")))


set3 = set1.intersection(set2)

print(sorted(list(set3)))