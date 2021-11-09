# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:44:22 2021

@author: 2-ogodboldvines
"""
import sys


allowedchar = ["!","$","%","^","&","*","(",")","-","_","=","+"]
def menu():
    option = int(input("Pick what you want to do:\n1.Check Password \n2. Generate Passwords\n3. Exit"))
    if (option == 1):
        check_password()
    elif (option == 2):
        generate_password()
    elif (option == 3):
        sys.exit(0)
    else:
        return print("Invalid Response")

def check_password():
    password = input("Input password: ")
    if len(password) >= 8 and <= 24:
        score += len(password)
        
    

def generate_password():
    
    

menu()