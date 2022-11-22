# Bid-Data-Prep
## From Scratch To The Professional

# Basicaly to Start a code we need to know the output and input the way it works.

NO_rook=143
DEC_rook=3.5
WORD_rook="Rocky Bai"
DRD_rook=False

print("Intiger Value of Rook",NO_rook)
print("Decimal Value of Rook",DEC_rook)
print("Word that Entered in the Dialogue Box",WORD_rook)
print("Does the Value Entered is Crt or Not",DRD_rook)

# As we how to get output of the value ,For now we can ee now o the which data type is the format

print("The Data type format of NO_rook",type(NO_rook))
print("The Data type format of DEC_rook",type(DEC_rook))
print("The Data type format of WORD_rook",type(WORD_rook))
print("The Data type format of DRD_rook",type(DRD_rook))

# And then now we are goonna see the type casting or changing the nature of the constant(numbers)

NO_rook=143.9
DEC_rook=3.5

# just by adding the prefix name (Float and Int) we can change the nature

print('The Value that changed from Intiger to Float ',float(NO_rook)) 
print('The Value that changed from Float to Intiger',int(NO_rook))

# Now see how to add a value to a stored value   

Sponge=120
Sponge=int(Sponge)+23
print("The Intiger that Crted or Edited after adding is",Sponge)  

# Now see how to add a value to a stored Decimal value  

Plugins=120.9
Plugins=float(Plugins)+23.4
print("The Float that Crted or Edited after adding is",Plugins)  
 
# Now see how to add a Word to a stored Word   

Pillar='I 1 2'
Pillar=str(Pillar)+' 4 Q'
print("The Word that Crted or Edited after adding is",Pillar)  

# now Let see how to get the user intput and to diplay in the output

Propeties_1=str(input("Enter the Properties need to by..."))
Propeties_2=int(input("Enter the Properties Count need to by..."))

# as we noted the header now the output section

print("The Properties need to by...",Propeties_1)
print("The Properties Count need to by...",Propeties_2)

# let see the data type of each input

print("the data type of given properties are",type(Propeties_1))
print("the data type of given properties count are",type(Propeties_2))
