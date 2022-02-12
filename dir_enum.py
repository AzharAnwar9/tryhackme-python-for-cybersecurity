import requests
import sys

dir_sub_list = open("wordlist2.txt").read()
directories = dir_sub_list.splitlines()

try:
    domain = sys.argv[1]
except:
    print("Domain not provided")
    print("Syntax : python3 dir_enum.py example.com")
    sys.exit(0)

for mydir in directories:
    dir_enum = f"http://{domain}/{mydir}.html"
    req = requests.get(dir_enum)
    if req.status_code == 404:
        #print(dir_enum, "Not Found")
        pass
    else:
        print(dir_enum)
