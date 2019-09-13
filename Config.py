import sys

def usrInput(msg):
    message = input(f"Enter a message to {msg}: ").lower()
    key = input("Enter the key value to use: ")
    showSteps = True if input("Show output of each step? (y or n): ") == "y" else False
    return message, key, showSteps

def config():
    print("\n************************************")
    print("*** Phishers of Men Cryptosystem ***")
    print("************************************\n")
        
    while True:    
        print("Options:")
        print(" ~ Encrypt a message (e)")
        print(" ~ Decrypt a message (d)")
        print(" ~ Exit (x)")
        user = input(": ").lower()

        if user.startswith('x'):
            print("Have a nice day!!")
            sys.exit()

        if user.startswith('e'):
            msg, key, steps = usrInput("encrypt")
            return True, msg, key, steps

        if user.startswith('d'):
            msg, key, steps = usrInput("decrypt")
            return False, msg, key, steps
        
        else:
            print("\nUnknown command")