l1 = [2,4,3]
l2 = [5,6,4]

a = int(''.join(str(x) for x in l1)[::-1]) + int(''.join(str(x) for x in l2)[::-1])

b = [x for x in str(a)[::-1]]
print(b)