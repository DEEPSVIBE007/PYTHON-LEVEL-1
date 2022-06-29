def swap(l, p1, p2):
   l[p1], l[p2] = l[p2], l[p1]
   return l

l = [1, 2, 3, 4, 5]

print("List:", l)

p1, p2 = 1, 2
print("New List:", swap(l, p1-1, p2-1))
