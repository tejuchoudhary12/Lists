List=["k","o","m","o","k"]
List1=[]
index=0
rev_len=len(List)-1
while index < len(List)//2:
    First_value = List[index]
    Last_value = List[rev_len]
    if First_value == Last_value:
        List1.append(List[rev_len])
        rev_len=rev_len-1
    index+=1
if First_value==Last_value:
    print("P")
else:
    print("NP")