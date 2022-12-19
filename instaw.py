import requests, time, os, re, colorama, json
from time import sleep
import sys
from colorama import Fore, Back, Style, init
import os,sys,time
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

try:
  from lolpython import lol_py 
  import pyfiglet
except:
  os.system("pip install lolpython")
  os.system("pip install pyfiglet")
  
re="\033[1;31m"
gr="\033[1;32m"
cy="\033[1;36m"
wi="\033[1,35m"

n = Fore.RESET
r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
grey = '\033[97m'
ye = Fore.YELLOW
colors = [r, lg, w, ye, cy]
info = lg + '[' + w + 'i' + lg + ']' + rs
error = lg + '[' + r + '!' + lg + ']' + rs
success = w + '[' + lg + '*' + w + ']' + rs
INPUT = lg + '[' + cy + '~' + lg + ']' + rs
plus = w + '[' + lg + '+' + w + ']' + rs
minus = w + '[' + lg + '-' + w + ']' + rs

n = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
ye = Fore.YELLOW
be = Fore.BLUE
colors = [lg, r, w, cy, ye]


def banner():
  os.system("clear")

  result = pyfiglet.figlet_format("    Instaw ", font = "slant"  )#chintoo
  lol_py(result) 
  lol_py('                                 Version: 1.0\n')
    
def getaccinfo():
    USERNAME = input(f'{INPUT}{cy} Enter Account Username: {r}')
    PASSWORD = input(f'{INPUT}{cy} Enter Account Password: {r}')
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o info')
    
def followbytag():
    USERNAME = input(f'{INPUT}{cy} Enter Account Username: {r}')
    PASSWORD = input(f'{INPUT}{cy} Enter Account Password: {r}')
    TAG = input(f'{INPUT}{cy} Enter Tag: {r}')
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-tag -t {TAG}')

def followbylocation():
    USERNAME = input(f'{INPUT}{cy} Enter Account Username: {r}')
    PASSWORD = input(f'{INPUT}{cy} Enter Account Password: {r}')
    LOCATION_ID = input(f'{INPUT}{cy} Enter Location ID: {r}')
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-location -t {LOCATION_ID}')
    
def followback():
    USERNAME = input(f'{INPUT}{cy} Enter Account Username: {r}')
    PASSWORD = input(f'{INPUT}{cy} Enter Account Password: {r}')
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o super-followback')
    
def followusersfromlist():
    USERNAME = input(f'{INPUT}{cy} Enter Account Username: {r}')
    PASSWORD = input(f'{INPUT}{cy} Enter Account Password: {r}')
    USER_LIST = input(f'{INPUT}{cy} Enter User List: {r}')
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-list -t {USER_LIST}')
    
def followusersfromlists():
    USERNAME = input(f'{INPUT}{cy} Enter Account Username: {r}')
    PASSWORD = input(f'{INPUT}{cy} Enter Account Password: {r}')
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-listss -t USER_LIST')
    time.sleep(60)
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-listsss -t USER_LIST')
    time.sleep(30)
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-listss -t USER_LIST')
    time.sleep(60)
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-listsss -t USER_LIST')
    time.sleep(30)
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-listss -t USER_LIST')
    time.sleep(60)
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o follow-listsss -t USER_LIST')

def unfollowback():
    USERNAME = input(f'{INPUT}{cy} Enter Account Username: {r}')
    PASSWORD = input(f'{INPUT}{cy} Enter Account Password: {r}')
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o super-unfollow')

def unfollowallusers():
    USERNAME = input(f'{INPUT}{cy} Enter Account Username: {r}')
    PASSWORD = input(f'{INPUT}{cy} Enter Account Password: {r}')
    os.system(f'python2 main.py -u {USERNAME} -p {PASSWORD} -o unfollow-all')
    
def setup():
    os.system(f'pkg install python2')
    os.system(f'pip2 install -r requirements.txt')
    


def main_menu():
    banner()
    print(f'{re}[1] Instagram Account Info:'+n)
    print(f'{gr}[2] Follow Instagram Account by Tag:'+n)
    print(f'{cy}[3] Follow Instagram Account by Location:'+n)
    print(f'{re}[4] FollowBack All Followers:'+n)
    print(f'{gr}[5] Follow Users from Lists:'+n)
    print(f'{cy}[6] UnfollowBack All Users:'+n)
    print(f'{re}[7] Unfollow All Users:'+n)
    print(f'{gr}[8] Setup Script:'+n)
    print(f'{cy}[9] Increase Followers:'+n)
    print(f'{gr}[10] Exit:'+n)
    
    
    a = int(input('\nEnter your choice: '))
    if a==1:
        getaccinfo()
    elif a==2:
        followbytag()
    elif a==3:
        followbylocation()
    elif a==4:
        followback()
    elif a==5:
        followusersfromlist()
    elif a==6:
        unfollowback()
    elif a==7:
        unfollowallusers()
    elif a==8:
        setup()
    elif a==9:
        followusersfromlists()
    elif a==10:
        quit()

main_menu()
        
