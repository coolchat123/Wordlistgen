import argparse
import sys
import time
us = True
def makeuserlist():
    print("any name or family name")
    namques = input()


def makepasswordlist():
    print("keywords about user (example : kyle, America, Football, School)")
    passques = input()
    lisques = []
    one = 0
    for line in passques:
        one += 1
        lisques.append(ques1 + str(one))
    print(lisques)
    print(lisques[0])

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

