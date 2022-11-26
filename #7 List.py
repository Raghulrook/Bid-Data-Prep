# Bid-Data-Prep
## From Scratch To The Professional

#List is sequensial data type which holds Many data types in it like Int, String, Float i.e-
Be = [1,'Witch',3.45]
print("",type(Be))

#Rather like array it is differ from it like array holds only Homogenous data type where as list is a Heterogeneous
#Syntax of list in python
A = [ ] #knows as empty list
print("",type(A))#by this u can know the data type of A

#See how to concade a values in the empty list
A = [ ]
A.append('String') #we can add a number using append comand but in the parenthesis we can't give camma or other variable but we acan give dat a type as it shown
A.append(4.65)
A.append(143)
print("",A)
print("",type(A))

#add 1-100 in a empty list
A = [ ]
for spare in range(1,11):
 A.append(spare)
print("The Element In The List\n",A) #taking the print out of the loop make more difference like when it is out of the loop the loop get over and the last value get print the output rather more line and time comsuming 
print("Here It is\n",type(A))

#see how to get the length of the list
A = [ ]
for spare in range(1,11):
 A.append(spare)
print("The Element In The List\n",A)
print("The Length Of The List\n",len(A))

#see how to the list value in the indexes are same or not
Aby = [1,'one.five',1.5]
Bvi = [1.5,'one.five',1] #output will be false because the index value is interchanged even the value in the list are same
print("The Value Of The Aby and Bvi ",Aby,Bvi)
print("Compare The Value Of The List Indises Aby and Bvi!",Aby == Bvi) #we can use the comperative operators to find the value (==,!=,<=,>=)

#how to print the list value one by one #1
print("The Element In The List")
for spare in range(1,11):
 print("",spare)

#see how to pick the ramdom or desired index stored value in a list
A = [ ]
for spare in range(1,51):
 A.append(spare)
print("The Element In The List Under Fifty - {}\n".format(A))
print("The Element Length - {}\n".format(len(A)))
Pinch = int(input("Enter The Desired No.Need To Take The List - ")) 
print("\nThe Desired Index Value In The List - ",A[Pinch])
 
# how to exchange the stored value in the list
A = ['Rocky','Bai']
print("The Real One",A)
A[0] = 'Raghul 👑'
print("\nBut The People Needed One",A)

#how to print the list value one by one using the list elements #2
A = ['Rocky 👑','Bai']
for spare in range(0,len(A)):
 print("",A[spare])
       
