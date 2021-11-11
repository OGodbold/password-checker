"""
Created on Tue Nov  9 11:44:22 2021
@author: 2-ogodboldvines
"""
import sys
import os



def check_password():
  score = 0
  password = input("Input password: ")
  if len(password) >= 8 and len(password) <= 24:
      score += len(password)
      upper = any(i.isupper() for i in password)
      lower = any(i.islower() for i in password)
      digit = any(i.isdigit() for i in password)
      if upper == True:
        score += 5
      elif lower == True:
        score += 5
      else upper == True:
        score += 5
      

    
  else:
      main()
      

        
    

def generate_password():
  main()

def main():
  allowedchar = ["!","$","%","^","&","*","(",")","-","_","=","+"]
  option = int(input("Pick what you want to do:\n1. Check Password \n2. Generate Passwords\n3. Exit \n "))
  if (option == 1):
    check_password()
  elif (option == 2):
    generate_password()
  elif (option == 3):
    sys.exit(0)
  else:
    print("Invalid Response")

main()
