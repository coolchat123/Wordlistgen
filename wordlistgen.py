import argparse
import sys
import time
import re
us = True
def makeuserlist():
    print("any name or family name")
    namques = input()

def makepasswordlist():
    print("Leave them empty if you don't know the answers.")
    print("Name of user?")
    name = input("> ")
    if re.match("^[0-9]*$",name):
      print("Name has to be letters.")
      name = input("> ")
    print("Lastname of user?")
    lastname = input("> ")
    if re.match("^[0-9]*$",lastname):
      print("Lastname has to be letters.")
      lastname = input("> ")
    print("Year of birth of user?")
    yearofbirth = input("> ")
    if re.match("^[A-Z-a-z]*$",yearofbirth) or len(yearofbirth) != 4:
      print("Year of birth has to be in numbers only and can only be 4 characters.")
      yearofbirth = input("> ")
    print("Name of Mom of user?")
    momname = input("> ")
    if re.match("^[0-9]*$",momname):
      print("Momname has to be letters.")
    print("Year of birth of mom?")
    momyear = input("> ")
    if re.match("^[A-Z-a-z]*$",momyear) or len(momyear) != 4:
      print("Year of birth has to be in numbers only and can only be 4 characters.")
      momyear = input("> ")
    print("Dad name of user?")
    dadname = input("> ")
    if re.match("^[0-9]*$",dadname):
      print("Dadname has to be letters.")
    print("Year of birth of dad?")
    dadyear = input("> ")
    if re.match("^[A-Z-a-z]*$",dadyear) or len(dadyear) != 4:
      print("Year of birth has to be in numbers only and can only be 4 characters.")
      dadyear = input("> ")
    lisques = []
    one = 0
    for x in range(10):
      one += 1
      lisques.append(name + str(one))
    for x in range(10):
      one += 1
      lisques.append(lastname + str(one))

    for x in range(10):
      one += 1
      lisques.append(momname + str(one))
    for x in range(10):
      one += 1
      lisques.append(dadname + str(one))

    lisques.append(lastname + yearofbirth)
    lisques.append(momname + momyear)
    lisques.append(dadname + dadyear)
    lisques.append(lastname + yearofbirth)
    lisques.append(name + yearofbirth)
    print(lisques)


def makepassuserlist():
    print("test")


parser = argparse.ArgumentParser(description='Welcome to Apsters wordlist generator')
parser.add_argument('-p', action='store_true', help='only password list')
parser.add_argument('-u', action='store_true', help='only username list')
parser.add_argument('-b', action='store_true', help='Password and Username list')

args = parser.parse_args()
if args.u:
    us = False
    makeuserlist()
if args.p:
    makepasswordlist()
    us = False
if args.b:
    makepassuserlist()
    us = False
if us == True:
    print("usage: wordlistgen.py [-h] [-p] [-u] [-b]\n\nWelcome to Apsters wordlist generator\n\noptional arguments:\n-h, --help  show this help message and exit\n-p          only password list\n-u          only username list\n-b          Password and Username list")

