# Bid-Data-Prep
# From Scratch To The Professional

# See how the If-Else is Works
Adam = 15
Eval = 30
if (Adam==Eval):
  print("Adam and Eval are have same things")
else:
  print("Adam and Eval are not have same things")
  
# See how the If-Else is Works on Words
Adam = 'on edge'
Eval = 'on edge'
if (Adam==Eval):
  print("Adam and Eval are have same things")
else:
  print("Adam and Eval are not have same things")
  
# See how the If-Else is Works on combination of Words and Numbers by user input
Adam = input("Enter a things that own for Adam") 
Eval = input("Enter a things that own for Eval") 
if (Adam==Eval):
  print("Adam and Eval are have same things")
else:
  print("Adam and Eval are not have same things")

# See how the Nested If-Else is Works
Good_Knight = 12
Mortein = 10
All_Out = 13
print("Mosquito Repellent that works Good Knight {}, Mortein {}, All Out {}".format(Good_Knight,Mortein,All_Out))
if (Good_Knight>Mortein):
    if (Good_Knight>All_Out):
        print("Mosquito Repellent that works for more than needed Good Knight {}".format(Good_Knight))
    else:
        print("Mosquito Repellent that works for more than needed All Out {}".format(All_Out))
elif (Mortein>All_Out):
   print("Mosquito Repellent that works for more than needed Mortein {}".format(Mortein))
else:
  print("Mosquito Repellent that works for more than needed All Out {}".format(All_Out))
  
# See how the Nested If-Else is Works in user input
Cello =input("Refillers by Cello Stand By Days ")
Hero = input("Refillers by Hero Stand By Days ")
Renolds = input("Refillers by Renolds Stand By Days ")
print("Refillers that works \nCello {}\nHero {}\nRenolds {}".format(Cello,Hero,Renolds))
if (Cello>Hero):
    if (Cello>Renolds):
        print("Refillers that works for more than needed Cello {}".format(Cello))
    else:
        print("Refillers that works for more than needed Renolds {}".format(Renolds))
elif (Hero>Renolds):
   print("Refillers that works for more than needed Hero {}".format(Hero))
else:
  print("Refillers that works for more than needed Renolds {}".format(Renolds))
