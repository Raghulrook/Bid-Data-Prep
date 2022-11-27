# Bid-Data-Prep
## From Scratch To The Professional

#List is sequensial data type which holds Many data types in it like Int, String, Float i.e-
Be = [1,'Witch',3.45]
print("",type(Be))

#Rather like array it is differ from it like array holds only Homogenous data type where as list is a Heterogeneous
#Syntax of list in python
A = [ ] #knows as empty list
print("\n",type(A))#by this u can know the data type of A

#See how to concade a values in the empty list
A = [ ]
A.append('String') #we can add a number using append comand but in the parenthesis we can't give camma or other variable but we acan give dat a type as it shown
A.append(4.65)
A.append(143)
print("\n",A)
print("",type(A))

#add 1-10 in a empty list
A = [ ]
for spare in range(1,11):
 A.append(spare)
print("\nThe Element In The List\n",A) #taking the print out of the loop make more difference like when it is out of the loop the loop get over and the last value get print the output rather more line and time comsuming 
print("Here It is\n",type(A))

#see how to get the length of the list
A = [ ]
for spare in range(1,11):
 A.append(spare)
print("\nThe Element In The List\n",A)
print("The Length Of The List\n",len(A))

# What will be the output ???
list8 = [ 1 , 2 , 50, "Shashank", [6,6,6] , "Raghul"]
print("\nLength of the Elements ",len(list8)) 

#see how to the list value in the indexes are same or not
Aby = [1,'one.five',1.5]
Bvi = [1.5,'one.five',1] #output will be false because the index value is interchanged even the value in the list are same
print("\nThe Value Of The Aby and Bvi ",Aby,Bvi)
print("Compare The Value Of The List Indises Aby and Bvi!",Aby == Bvi) #we can use the comperative operators to find the value (==,!=,<=,>=)

#how to print the list value one by one #1
print("\nThe Element In The List One By One")
for spare in range(1,11):
 print("",spare)

#see how to pick the ramdom or desired index stored value in a list
A = [ ]
for spare in range(1,51):
 A.append(spare)
print("\nThe Element In The List Under Fifty - {}\n".format(A))
print("The Element Length - {}\n".format(len(A)))
Pinch = int(input("Enter The Desired No.Need To Take The List - ")) 
print("\nThe Desired Index Value In The List - ",A[Pinch])
 
# how to exchange the stored value in the list
A = ['Rocky','Bai']
print("\nThe Real One",A)
A[0] = 'Raghul 👑 '
print("\nBut The People Needed One",A)

#how to print the list value one by one using the list elements #2
A = ['Rocky 👑','Bai']
for spare in range(0,len(A)):
 print("\n",A[spare])
       
#how to use the append() and extend() in the list function to include it as one of the index
A = ['Apple','Ball','Cat']
B = ['Dog','Eagle','Fish']
C = ['Apple','Ball','Cat']
A.append(B)# which is used to add a list but not in a individual index
print("\nLyric With 404... ",A)
print("Length Is",len(A))
C.extend(B)# Where as this one is used to add a list with a individual index for element in the list
print("\nLyric WithOut 404... ",C)
print("Length Is",len(C))

#Now see what is slicing in the list 
#Syntax - List[start:end:step]
BF = ['👋 💈 💧 ']
print("\n BF Value -",BF[::])#The same which we follow in the for loop is used in here 
#Leaving the Start, End, Step value blank is also feasible cuz the interprator take value as the default 
GF = [1,'One',2,'Two',3,'Three']
print("\n GF Value -",GF[0:6:1])#By known value we can 
BB = [1,'One',2,'Two',3,'Three']
print("\n BB Value With Words Only -",BB[1:6:2])#let start with One, End with Three and Step with +2 
GF = [1,'One',2,'Two',3,'Three']
print("\n GF Value Got Reverse -",GF[::-1])#Let print in reverse, By using Step value as -1
BB = [1,'One',2,'Two',3,'Three']
print("\n BB Value Got Reverse With Words Only -",BB[-1::-2])#Let print in reverse with Start of 1 and  Step difference of 2

