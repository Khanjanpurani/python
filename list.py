a=[1,2,3,5,8,9,0,6,52,5,44]
print(a[0])
print(len(a))
if 3 in a:
    print('yes')

b=["k","d","d"]
a.extend(b)
print(a)
del a[0]
print(a)
for num in a:
    print(num)

for i in range(0,11):
    print(i)

a.reverse()
print(a)