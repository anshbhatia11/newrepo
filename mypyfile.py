print("hello, this is a github repo")

#This is entirely focussing on hactober fest
#Added a new feature for you brother
# Three sides of the triangle is a, b and c:  
a = float(input('Enter first side: '))  
b = float(input('Enter second side: '))  
c = float(input('Enter third side: '))  
  
# calculate the semi-perimeter  
s = (a + b + c) / 2  
  
# calculate the area  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)   


#String reversal
def my_function(x):
  return x[::-1]

mytxt = my_function("I wonder how this text looks like backwards")

print(mytxt)
