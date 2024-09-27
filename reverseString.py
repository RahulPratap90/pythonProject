#1st way to reverse..

'''i =  input("Enter String to Reverse:-")
output = i[::-1]
print(output)'''
from numpy.ma.core import outer

# 2nd way

'''s='rahul'
r=reversed(s)
output=''.join(r)
print(output)'''

# 3rd way
'''s = input("Enter the String:-")
output = ''
i = len(s)-1
while i>=0:
    output = output+s[i]
    i = i-1
print(output)'''

# 4th way

'''s = input("Enter the String:-")
l = s.split()
#l1 = l[::-1]
#l1 = l.reverse(s)
print(l1)
print( ' '.join(l1))'''

#5th way

'''s = input("Enter the String:-")
l = s.split()
l1 = []
for word in l:
    l1.append(word[::-1])
print(l1)
print(' '.join(l1))'''

# 6th way

s = input("Enter the String:-")
l = s.split()
i = 0
l1 = []
while i<len(l):
    if i%2==0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i=i+1
print(' '.join(l1))
print('hello')

