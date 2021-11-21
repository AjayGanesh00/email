while True :
    try :
        email = input('''
Enter Your Email : ''').lower()

        email = email.replace(" ","")

        username = email[:email.index('@')]

        domain = email[email.index("@")+1:]

        ask = input('''
Do You Need Your Domain/Username/Both : ''').lower()

        if ask == "domain" :
            print(f'''
domain = {domain}''')
        elif ask == "username" :
            print(f'''
username = {username}''')
        else :
            print(f'''
username = {username}

domain = {domain}''')

        print('''
Do You want to enter a new mail ''')

        ans = input('''
Say Yes Or No : ''').lower()

        if ans == "no" :
            break

    except ValueError :
        print('''
Enter Your Email Again It Seems To Be Wrong''')

print(f'''
Copyrights Deserve To Ajay Ganesh''')
