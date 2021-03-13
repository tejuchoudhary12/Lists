num=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# index=0
# max=num[0] 
# while index<len(num):
#     m=num[index]
#     if m>max:
#         max=m
#     num.remove(max)
#     break
# while index<len(num):
#     m=num[index]
#     if m>max:
#         smax=m
#     index+=1
# print("max",smax)

max=num[0]
secmax=num[1]
i=0
while i<len(num):
    if num[i]>max:
        secmax=max
        max=num[i]
    elif num[i]>secmax:
        secmax=num[i]
    i+=1
print("So the second max number:", secmax)