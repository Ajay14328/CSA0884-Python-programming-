first={1,2,3,4,5,6}
second={4,5,6,7,8,9}
intersection=first.intersection(second)
print(intersection)
for i in intersection:
    first.remove(i)
print(first)
