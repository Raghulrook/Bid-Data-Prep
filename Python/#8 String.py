# Bid-Data-Prep
## From Scratch To The Professional

#Sytnax - "" - ''
#Create a string in Python
Str1 = "Nepal"
print(Str1)

Str2 = "Nepal's"#The Usage of "" and '' is under same condition but the "" helps to a stringwhich contains plural like Nepal's to print we use ""  
print(Str2)

Str3 = 'She has a "Good" Melons Garden'
print(Str3)

#Use length function
print("length of the string : ",len(Str3))#As same to find the length but in this the function count on every Char, Space and Symbols

#How to write multiline string
Str4 = '''\nCuz Of Which#By using ''' ''' we can add multiple line of sting in case adding paragraph
U Become A Witch
It Made Me Think That Ur 
"A BITCH"'''
print(Str4)

#String concatenation
Str5 = "\n\tAdam Lov-"
Str6 = "De Eve"
print(Str5 + Str6)#as the function used in list and normal operator

#String comparsion?
Str7 = "Adam Lo-"
Str8 = "Ve Eve"
print("\n",Str7 == Str8)#as the function used in list and normal operator

#How to print the each character from the string
for char in Str8:
    print(char)

print(Str8[0])
print(Str8[1])
print(Str8[2])
print(Str8[3])
print(Str8[4])
print(Str8[5])

#Update the 4th character in the string by M
Str9 = "Loading Pure Breed Of Pit Bulls In The Shelter"
# Str9[3] ="M"
print("\n",Str9)#we can't change the element in the string index

#Convert string into lower case
print("\n",Str9.lower())
#though we can't upper or lower case a particular index in the element
#Convert string into upper case
print("\n",Str9.upper())

#Other functionalities will be same as list like Slicing etc
