list=["t","e","j","a","e","t"]
flag=True
i=0
rev_index=len(list)-1
while (i<len(list)):
    if (list[i] !=list[rev_index]):
        flag=False
        break
    elif (i==rev_index):
        break
    i+=1
    rev_index-=1
if (flag):
    print("P")
else:
    print("NP")

