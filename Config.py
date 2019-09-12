import sys

def usrInput(msg):
    message = input(f"Enter a message to {msg}: ")
    key = input("Enter the key value to use: ")

    return message, key

def config():
    print("\n****************************")
    print("Phishers of Men Cryptosystem")
    print("****************************\n")
    print("Options:")
    print(" ~ Encrypt a message (e)")
    print(" ~ Decrypt a message (d)")
    print(" ~ Exit (x)")
    user = input(": ").lower()

    if user.startswith('x'):
        print("Have a nice day!!")
        sys.exit()

    if user.startswith('e'):
        msg, key = usrInput("encrypt")
        return True, msg, key

    if user.startswith('d'):
        msg, key = usrInput("decrypt")
        return False, msg, key