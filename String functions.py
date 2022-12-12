#String functions

x='my name is xyz'
print(x.capitalize())
print(x.upper())
print('python programming'.lower())
print(x.title())
print('My Name Is Xyz'.swapcase())

#
#
x='hello'
print(x.split())
y='hello my name is xyz'
print(y.split())

#
#
print(x.center(9,'*'))

#
#
x='abc abc xyz xyz def'
print(x.count('ghi'))
print(x.count('abc'))
print(x.count('def'))
print(x.count('xyz'))

#
#
y='hello world'
print(y.replace("hello",'hi'))

#
#
ip=['192','165','0','1']
b='.'
print(b.join(ip))

#
#
#Write a program to demonstarte string methods using a user input string.Follow the instruction given in the comment lines in the below program , and print the result as shown in the example
str=input()
print(str.upper())
print(str.title())
print(str.split())
print(str.center(25,'%'))
print(str.lower())
str2='@'
print(str2.join(str))
print(str.replace('Strings','Tuples'))

#
#
print('ABC'.isupper())
print('abc'.islower())
print('abc'.isalpha())
print('abc123'.isalpha())
print('abc123'.isalnum())
print('123'.isdigit())

#
#
##Write a program to triverse or string a string while using while loop
x=input()
i=0
while i<len(x):
    print(x[i],end='')
    i=i+1
#
#
#Write a program to print every 2nd character using for loop
bc=input("enter")
for i in range(0,len(bc),2):
    print(bc[i],end="")





