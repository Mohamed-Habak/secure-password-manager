import secrets
import os
import hashlib
import requests
from cryptography.fernet import Fernet

def main():
    while True:
        choice = input("what do you want to do?\n"
        "- Press 0 to quit the program\n"
        "- Press 1 to check your password strength\n"
        "- Press 2 to generate a random powerful password\n"
        "- Press 3 to check if your password has been breached\n"
        "- Press 4 to save your password\n"
        "- Press 5 to load all of your saved passwords\n")

        if choice == "0":
            break

        elif choice == "1":
            password = input("Input your password here to check its strength: ")
            print(check_strength(password))

        elif choice == "2":
            while True:
                try:
                    x = int(input("to generate a password please type how many letters it should have (we recommend that the password be longer than 12 letters): "))
                    password = generate_password(length=x)
                    print("Generated password:", password)

                    while True:
                        save = input("Do you want to save this password for later use? (y/n): ")

                        if save.lower() == "y":
                            print(save_password(password))
                            break
                        elif save.lower() == "n":
                            print("Password not saved.")
                            break  
                        else:
                            print("Please enter a valid answer.")


                    break
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "3":
            password = input("Input your password here to check if your password has been breached: ")
            print(check_breach(password))
            

        elif choice == "4":
            password = input("Input your password here to save it: ")
            print(save_password(password))
        
        elif choice == "5":
            print("Your saved passwords: ")
            print(load_passwords())

        else:
            print("Please pick a valid number.")


def check_strength(password):
    score = 0
    results = {"length": "", "has_upper": "", "has_lower": "", "has_digit": "", "has_symbol": "", "score": ""}
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)


    if len(password) >= 8:
        score += 20
        length = f"longer than 8 characters ✔️"
        results["length"] = length
    else:
        length = f"longer than 8 characters ❌"
        results["length"] = length
    
    if has_upper:
        score += 20
        results["has_upper"] = "Contains uppercase ✔️"
    else:
        results["has_upper"] = "No uppercase ❌"

    if has_lower:
        score += 20
        results["has_lower"] = "Contains lowercase ✔️"
    else:
        results["has_lower"] = "No lowercase ❌"

    if has_digit:
        score += 20
        results["has_digit"] = "Contains digit ✔️"
    else:
        results["has_digit"] = "No digit ❌"

    if has_symbol:
        score += 20
        results["has_symbol"] = "Contains symbol ✔️"
    else:
        results["has_symbol"] = "No symbol ❌"

    if score < 40:
        results["score"] = f"Total score: {score} (weak)"
    elif 40 <= score <= 80:
        results["score"] = f"Total score: {score} (medium)"
    else:
        results["score"] = f"Total score: {score} (strong)"

    return "\n".join(results.values())




def generate_password(length=16):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    password = "".join(secrets.choice(characters) for _ in range(length))
    return(password)




def check_breach(password):
    hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()

    prefix = hash[:5]
    sufix = hash[5:]
     
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")

    if response.status_code != 200:
        raise RuntimeError("Error fetching data from HIBP API")
    
    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == sufix:
            return "this password has been leaked"
    
    return "Safe. not found in known breaches"





def save_password(password, filename="passwords.txt", keyfile="keys.txt"):
    try:

        if os.path.exists(keyfile):
            with open(keyfile, "rb") as kfile:
                key = kfile.read()
        else:
            key = Fernet.generate_key()
            with open(keyfile, "wb") as kfile:
                kfile.write(key)


        cipher = Fernet(key)
        
        encrypted = cipher.encrypt(password.encode())

        with open(filename, "ab") as file:
            file.write(encrypted + b"\n")

        return "Password saved successfully!"
    
    except Exception:
                    return "There was an error saving your password"
    



def load_passwords(filename="passwords.txt", keyfile="keys.txt"):
    try:
        with open(keyfile, "rb") as kfile:
            key = kfile.read()

        cipher = Fernet(key)

        with open(filename, "rb") as file:
            passwords = file.readlines()

        decrypted = [cipher.decrypt(password.strip()).decode() for password in passwords]
        return decrypted
    
    except FileNotFoundError:
        return "No saved passwords found"
    
    except Exception:
        return "Error getting back saved passwords"



if __name__ == "__main__":
    main()