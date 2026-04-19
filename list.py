val = list(map(int,input('Enter integer values : ').split()))

print('List values : ', val)

even = 0
odd = 0

for i in val:
    if (i%2 == 0):
        print("even:", i)
        even = even+1
    else:
        print("odd : ", i)
        odd = odd+1

print("Odd numbers in  list are : ", odd)
print("Even numbers in list are : ", even)