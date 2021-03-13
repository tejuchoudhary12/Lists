List=[1,0,0,1,1,0,1,1]
i=0
p=0
sum=0
lenght=len(List)-1
while i<len(List):
    m=List[lenght]   
    p=(2**i)*m
    lenght-=1
    i+=1
    sum+=p
print(sum)