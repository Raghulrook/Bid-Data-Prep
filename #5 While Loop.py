# Syntax
# while exp:
#     statements

# write a program to print the table of 9
num = 9
counter = 1

#Example on While Loop Example On Tables 
while counter<=10: # Either True or False
    ans = num * counter
    print(num,' * ',counter,' = ',ans)
    counter = counter + 1

# What will happen if counter not incremented??
#some infinite while loop example
while counter<=10: # Either True or False
    ans = num * counter
    print(num,' * ',counter,' = ',ans)
    #counter = counter + 1
# 9  *  1  =  9 -> 

#some infinite while loop example
# What will happen?
while True:
    print("iNeuron")
