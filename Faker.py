  from os import system

# Check the requirements

try:
  from ast import For
  from faker import Faker
  from colorama import Fore
except ImportError:
   system("pip install ast")
   system("pip install os ")
   system("pip install colorama ")
   system("pip install faker")
   exit("\n\nRun script Again")

# Start APP

os.system("cls")
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
