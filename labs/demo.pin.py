#max 3 attempts
import getpass

master_pin = "0123"
pin = None
attempts = 0
while pin != master_pin and attempts < 3:
    pin = getpass.getpass("Enter PIN: ")
    if pin == master_pin:
        print("Valid PIN")
        break
    else:
        print("invalid PIN")
        attempts += 1

print ("Done.")





