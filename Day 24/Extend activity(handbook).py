l=[7,4,2,6,9,1,5]
a= l.append(3,8) # generates an error 
a= l.extend(3,8) # generates an error 
a= l.extend([3,8])
print(l)

l1=[3,6,2]
l2=[9,7,1]
l1.extend(l2)
print(l1)