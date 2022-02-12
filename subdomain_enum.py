import requests
import sys

domain_file_handle = open("wordlist2.txt").read()
sub_domains = domain_file_handle.splitlines()

try:
    domain = sys.argv[1]
except:
    print("Domain not provided")
    print("Syntax : python3 subdomain_enum.py example.com")
    sys.exit(0)

for sub_doms in sub_domains:
    main_domain = f"http://{sub_doms}.{domain}"

    try :
        requests.get(main_domain)
    except requests.ConnectionError:
        print(main_domain, "Not found")
        pass
    else:
        print(main_domain)
