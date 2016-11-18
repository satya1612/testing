#the starting two numbers for a,b,c must be the same for all!
T=3
print T
a=input() 
b=input()
c=input()
d=a/100
e=b/100
f=c/100
g=a%100
h=b%100
i=c%100
if g-d==10 or h-e==10 or i-f==10:
	print "Right"
if g-d==-10 or h-e==-10 or i-f==-10:
	print "left"
if g-d==-1 or h-e==-1 or i-f==-1 :
	print "up"
if g-d==1 or h-e==1 or i-f==1:
	print"down"
else:
	print"sad"



