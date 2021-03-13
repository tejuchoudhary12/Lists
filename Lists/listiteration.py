num=[50, 40, 23, 70, 56, 12, 5, 10, 7] 
# num.sort()
# print(num)
# print(num[4:5])

# length=len(num)
# count=0
# less_20=0
# more_40=0
# while count<length:
#     n=num[count]
#     if n<20:
#         less_20+=1
#     else:
#         more_40+=1
#     count+=1
# print("less_then_20:"+ str(less_20))
# print("more_then_40:"+ str(more_40))

i=0
while i<len(num):
    if num[i]>20 and num[i]<40:
        a=num[i]
        print(a)
    i+=1  