import os

print('''
░█████╗░██╗░░██╗███████╗██╗░░░░░██╗░░░██╗██████╗░░█████╗░███╗░░██╗          █████╗░░██████╗
██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░╚██╗░██╔╝██╔══██╗██╔══██╗████╗░██║         ██╔══██╗██╔════╝
███████║░╚███╔╝░█████╗░░██║░░░░░░╚████╔╝░██████╔╝██║░░██║██╔██╗██║         ██║░░██║╚█████╗░
██╔══██║░██╔██╗░██╔══╝░░██║░░░░░░░╚██╔╝░░██╔══██╗██║░░██║██║╚████║         ██║░░██║░╚═══██╗
██║░░██║██╔╝╚██╗███████╗███████╗░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ██╗    ╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═╝    ░╚════╝░╚═════╝░
''')

print('''
[1] continue with Setup
[2] Ive Already done Setup
''')
setup = input('[?]: ')

match setup:
    case '1':
        name = input(str('Please enter Your User name To Display: '))
        pas = input(str('Please enter your password to Login: '))

        with open('user/username.txt', 'w') as f:
            f.writelines(name)

        with open('user/password.txt', 'w') as f:
            f.writelines(pas)
        print('Setup complete!!!')
        input('Press enter to close window: ')

    case '2':
        login_pass = open('user/password.txt')
        login_name = open('user/username.txt')
        l_p = login_pass.read()
        l_n = login_name.read()


while True:
    login = input(str('Please Enter your password: ' + l_n + ': '))
    if login == l_p:
        os.startfile('home.py')
        break
    else:
        print('OOOps wrong password! ')
