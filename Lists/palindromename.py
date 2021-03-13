# place=["m","o","m"]
# place=['m','o','t','o','j','m']
i=0
list1=[]
a=len(place)-1
while a>=0:
    if place[i]==place[a]:
        list1.append(place[i])
        i+=1
    a-=1 
print(list1)
if list1==place:
    print("it is palindrome")
else:
    print("it is not palindrome")
