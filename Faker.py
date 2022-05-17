from os import system
from ast import For
from faker import Faker
import os
from colorama import Fore
import platform 

# Start APP
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

userput = input(Fore.YELLOW+ "Please Enter an Language and Location [Example ~> en_US]: "+Fore.RESET)
faker = Faker(userput)

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
print("------------Faker------------")