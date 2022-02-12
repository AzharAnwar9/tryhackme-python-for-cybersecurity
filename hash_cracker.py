import hashlib
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Hash Cracker")
print(ascii_banner)

hash_input = str(input("Enter the hash value you want to crack :"))

with open("wordlist2.txt", "r") as file :
    for line in file.readlines():
        hash_object = hashlib.sha256(line.strip().encode())
        hashed_password = hash_object.hexdigest()

        if hashed_password == hash_input :
            print("Clear Text :", line.strip())
            exit(0)
