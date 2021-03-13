# num= [50, 40, 23, 70, 56, 12, 5, 10, 7] 
# num.sort()
# print(num)
# print("max:", num[-1])

index=0
max=num[0]
while index<len(num):
    m=num[index]
    if m>max:
        max=m
    index+=1
print("max no. is:", max)

