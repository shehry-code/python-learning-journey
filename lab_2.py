val = list(map(int,input('Enter integer values : ').split()))
max = 0
for i in val:
    if (i>max):
        max = i


print("maximum value : ", max)