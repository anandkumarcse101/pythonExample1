#list data type
#1. []
#Mutable
#Ordered(indexing)
#different data type(heterogeneous objects are allowed)
#duplicate allwed

li=[10,20,20,30,40]
print(li[1:3])
li[0]=100#inserting 100 at 0 indext
print(li[0])
print(li)

for i in li:
    print(i)
#operation
li.append("Aditya")
print(li)
li.remove(20)
print(li)

li2=li*2
print(li2)

#tuple data type
#immutable
#()

t=(10,20,30,40)


#range data Type
r=range(10)#0,1,2,3,4,5,6,7,8,9

for x in r:
    print(x)

r1=range(10,20)#10,11,12,13,14,15,16,17,18,19
for y in r1:
    print(y)
r2=range(10,20,2)#10,12,14,16,18
for rohan in r2:
    print(rohan)

#set data type
#No duplicate
#{}
#No indexing
#Mutable
s={100,0,10,200,10,'durga'}
print(s)
s.add("Anand Kumar")
print(s)

#dic data type
#key-value pair
d={101:'Anand',102:"Rohan",103:"Akash"}
d[101]="Aditya"
print(d)

d1={}
print(d1)
d1[101]="Anand"
d1[202]="Rohan"
d1[203]="Akash"
print(d1)

#None data type
name=None
print(name)

#Escape characters:
strin="Anand\tKumar"
print(strin)

#constants
PI=3.14








