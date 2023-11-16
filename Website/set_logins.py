from hashlib import sha256
while True:
    print('Enter admin email address')

    email = input()

    print('Is this the correct email? Y/n\n' + email)

    correct = input()
    
    if(correct == 'Y' or 
       correct == 'y' or
       correct == ''):
        email_hash = sha256(bytes(str(email), 'utf-8')).hexdigest()
        try:
            file = open('LOGIN_HASH', 'a')
        except FileNotFoundError:
            open('LOGIN_HASH', 'x')
            file = open('LOGIN_HASH', 'a')
        file.write(email_hash + '\n')
        file.close()
        break
