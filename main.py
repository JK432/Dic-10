# Write a Python program to demonstarte the dictionary functions functions and operations

#Creating new dictionary from previous values
d1={1:"India",2:"America",3:"Britain",4:"Spain"}
d2={1:"Bangladesh",2:"Dubai",3:"Nepal"}
contry =d1.copy()
scontry=d2.copy()
print(contry )
print(scontry)

#Updating Dictionary	
d1.update({5:"Black current"})
print(d1)

#Deleting keys from dictionary
del d2[3]
print(d2)

#Printing as key value pairs
print("The output:-",list(d1.items()))

#Sorting dictionary
d4={2:"How",4:"Why",1:"When",3:"What"}
d3=dict(sorted(d4.items()))
print(d3)

#In-built functions

#1.len
print("Length of d1:",len(d1))
#2.Update
d3.update(d1)
print(d3)