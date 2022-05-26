# Start (Import libraries)

from cmath import exp
from os import system
from ast import For
import platform
import sys
import os
try:
   from faker import Faker
   from colorama import Fore
except:
   print("Installing prerequisites")
   print("Installing prerequisites")
   system("pip install faker")
   system("pip install colorama")
   exit('\n',"Run script Again")

# End (Import libraries)

# Start (Banner & Clearing)

def clear():
   result = platform.uname()[0]
   if result == "Windows":
      system("cls")
   elif result == "Linux":
      system("clear")
clear()

print(Fore.RED+ """
  ____|             |                
  |     _` |   __|  |  /   _ \   __| 
  __|  (   |  (       <    __/  |    
 _|   \__,_| \___| _|\_\ \___| _|    
                                     """+Fore.RESET)

# End (Banner & Clearing)

# Start (APP & Get Input From User)

try:
   userput = input(Fore.YELLOW+ "Please Enter an Language and Location [Example ~> en_US]: "+Fore.RESET)
   faker = Faker(userput)
except:
    print(Fore.RED+ "You canceled the program!"+Fore.RESET)
    sys.exit()

#### GENERATE Fake Variables ###########
fullname = faker.name() # Random Full Name
username = faker.user_name() # Random Username
password = faker.password() # Random Password
email = faker.email() # random Email
job = faker.job() # Random JOB
address = faker.address() # Random Address
favorite_color = faker.color_name() # Random Favorite Color
website = faker.domain_name() # Random Website Domain

###### SHOW Fake Variables #########


print('\n',Fore.CYAN+ "Language & Location:="+Fore.RESET,Fore.GREEN+ userput+Fore.RESET,'\n')
print("------------Faker------------",'\n')
print(". Full Name : {}\n".format(fullname))
print(". Username : {}\n".format(username))
print(". Password : {}\n".format(password))
print(". Email : {}\n".format(email))
print(". Job : {}\n".format(job))
print(". address : {}\n".format(address.replace("\n" , " - ")))
print(". Favrite Color : {}\n".format(favorite_color))
print(". Web Site : {}\n".format(website))

filefake = open("Faker.txt","w",encoding="utf-8")
filefake.write("Full Name: "+ fullname)
filefake.write("\n \n User Name: "+ username)
filefake.write("\n \n Password: "+ password)
filefake.write("\n \n Email "+ email)
filefake.write("\n \n Job: "+ job)
filefake.write("\n \n Address: "+ address)
filefake.write("\n \n Favrite Color: "+ favorite_color)
filefake.write("\n \n Web Site: "+ website)
filefake.close()
print('\n',Fore.GREEN+". The information created in the 'Faker.txt' file was saved!"+Fore.RESET,'\n')

print("------------Faker------------")

# End (APP & Get Input From User)