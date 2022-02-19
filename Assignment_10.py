import os
from os import mkdir



# get directory and filename
directory = input("Which directory would you like to save in? ")

    # validate if directory exists
try:    #open file for writing
    os.mkdir(f"{directory}")
except FileExistsError:
	pass
    
file = input("Please enter the filename. ")
with open(f'{directory}/{file}.txt', 'w') as fp:
	pass
name = input("Please enter your name. ")
address = input("Please enter your address. ")
phone =  input("Please enter your phone #. ")
data = (f"{name}, {address}, {phone}")

with open(f"{directory}/{file}.txt", "w") as file_object:
	file_object.write(data)
	


with open(f"{directory}/{file}.txt") as f:
	for line in f:
		print(line)
		



    

