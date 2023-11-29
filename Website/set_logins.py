from hashlib import sha256
from os import remove

#Remove file if emails need to be reset
print('Reset login file? Y/n')
reset = input()
if(reset == 'Y' or 
   reset == 'y' or
   reset == ''):
    try:
        remove('LOGIN_HASH')
    except:
        print('File does not exist')
print('Add an admin email address? Y/n')
add_email = input()
if(add_email == 'Y' or 
   add_email == 'y' or
   add_email == ''):
    
    while True:
        print('Enter admin email address')

        email = input()

        print('Is this the correct email? Y/n\n' + email)

        correct = input()

        if(correct == 'Y' or 
           correct == 'y' or
           correct == ''):
            email_hash = sha256(bytes(str(email).strip(), 'utf-8')).hexdigest()
            try:
                fileW = open('LOGIN_HASH', 'a')
            except FileNotFoundError:
                open('LOGIN_HASH', 'x')
                fileW = open('LOGIN_HASH', 'a')
            #Check if hash is present in file
            fileR = open('LOGIN_HASH', 'r')
            hashes = fileR.readlines()
            hash_not_present = True
            for line in hashes:
                if(email_hash == line.strip()):
                    print('Email hash already in file.')
                    hash_not_present = False
                    break
            fileR.close()
            #Enter email is not present in file
            if(hash_not_present):
                fileW.write(email_hash + '\n')
                fileW.close()
            #Check if another email should be entered
            print('Enter different admin email? Y/n')
            new_email = input()
            if(correct != 'Y' or 
               correct != 'y' or
               correct != ''):
                break
