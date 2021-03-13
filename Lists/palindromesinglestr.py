list1=["t","e","j","u"]
list2=[]
index=0
back_len=len(list1)-1
while index<len(list1):
    start_value=list1[index]
    finish_value=list1[back_len]
    if start_value==finish_value:
        list1.append(list1[back_len])
        back_len-=1
    index+=1
if list1==list2:
    print("it is a palindrome")
else:
    print("it is not a palindrome")