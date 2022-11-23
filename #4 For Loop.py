# Bid-Data-Prep
## From Scratch To The Professional

#let see how the for loop works on python
#syntax
X=[1,2,3]
for num in X:#num is a variable to store value
    print("",num)
    
#let see how the for loop works on string
#syntax
X=['Apple','Ball','Coal']
for num in X:#num is a variable to store value
    print("",num)
    
#let see how the for loop works on Combine
#syntax
X=[5.01,'Apple',123]
for num in X:#num is a variable to store value
    print("",num)
    
#let see how the for loop works on Combine in user input
#syntax
Name,Age,Birth_Date,Zodiac_Sign=input("Enter the Bio Name ",),input("Enter the Bio Age ",),input("Enter the Bio Birth Date ",),input("Enter the Bio Zodiac Sign ",)
for num in Name,Age,Birth_Date,Zodiac_Sign:#num is a variable to store value
    print("",num)

# range(starting, Ending, increment or decrement)
#Write a code to print numbers from 1 to 10
for num in range(1,11): #rang(1,11) -> [1,2,3,4,5,6,7,8,9,10]
    print(num)

#Write a code to print numbers from 1 to 10 using 2 steps
#  OR
#Example to print odd numbers starting from value 1
for num in range(1,11,2):
    print(num)

#Write a program to print numbers from 10 to 1
for num in range(10,0,-1):
    print(num)

#Write a program to calculate the sum of given list elements using for loop
a=[4,8,-2,10,5] 
b=0
for c in a : 
  b+=c 
  print ("The addition Of all No. in list =",b)

# 0  + 4 = 4
# 4 + 8 = 12
# 12 + (-2) = 10
# 10 + 10 = 20
# 20 + 5 = 25
