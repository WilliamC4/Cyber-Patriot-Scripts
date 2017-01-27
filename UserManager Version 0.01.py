#Python User Manager 
#Version 0.01
#William Cleghorn

import os
import re

commonUsers = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']

os.system("clear")
tempUserList  = []
authUsers = []
defUsers = []
stringAuthUsers = ""
stringdefUsers = ""

def main():
	os.system("clear")
	tempUserList  = []
	authUsers = []
	defUsers = []
	stringAuthUsers = ""
	stringdefUsers = ""
	
	tempUserList = os.system("ls")
	
	stringdefUsers = raw_input("Enter Default Users (Seperate With Spaces): ")
	stringAuthUsers = raw_input("Enter Authorized Admin Users (Seperate With Spaces): ")
	
	defUsers = re.sub("[^\w]", " ", stringdefUsers).split()
	authUsers = re.sub("[^\w]", " ", stringAuthUsers).split()
	
	print("Default Users: ")
	print(defUsers)
	print("Admin Users: ")
	print(authUsers)
main()




