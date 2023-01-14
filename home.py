import time
import os
import socket
import psutil


battery = psutil.sensors_battery()
login_pass = open('user/password.txt')
login_name = open('user/username.txt')
l_p = login_pass.read()
l_n = login_name.read()

print('''
░█████╗░██╗░░██╗███████╗██╗░░░░░██╗░░░██╗██████╗░░█████╗░███╗░░██╗          █████╗░░██████╗
██╔══██╗╚██╗██╔╝██╔════╝██║░░░░░╚██╗░██╔╝██╔══██╗██╔══██╗████╗░██║         ██╔══██╗██╔════╝
███████║░╚███╔╝░█████╗░░██║░░░░░░╚████╔╝░██████╔╝██║░░██║██╔██╗██║         ██║░░██║╚█████╗░
██╔══██║░██╔██╗░██╔══╝░░██║░░░░░░░╚██╔╝░░██╔══██╗██║░░██║██║╚████║         ██║░░██║░╚═══██╗
██║░░██║██╔╝╚██╗███████╗███████╗░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ██╗    ╚█████╔╝██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝╚══════╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ╚═╝    ░╚════╝░╚═════╝░
''')

print('Welcome ' + l_n)
print('The date is: ' + time.strftime("%m/%d/%y"))
print('The Battery level Is: ')
print(battery.percent, '%')
print('''
    [1]  To Open BROWSER
    [2]  To Open Text Editor
    [3]  To Open My Pc
    [4]  To Configure and Open Bios
    [5]  To Open Task Manager
    [6]  To Open Telegram
    [7]  To Open Recycle bin
    [8]  To Open Mail
    [9]  To Open Terminal
    [10] To Write Note
    [11] To Read your notes
    [exit] To Close os Safley
    ''')

while 1:
    select = input('[?]: ')

    match select:
        case '1':
            os.startfile('config.py')

        case '2':
            os.startfile('editor.py')

        case '3':
            os.system('explorer')
            os.startfile('User@WIN-O45VIBESU8F MINGW64 ~/Desktop')

        case '4':
            while 1:
                b_login = input(
                    str('Please Enter The Password To ' + l_n + " To Open Bios: "))
                if b_login == l_p:
                    print('Opening Bios...')
                    host_name = socket.gethostname()
                    host_ip = socket.gethostbyname(host_name)
                    print('[1] USER NAME: ' + l_n)
                    print('[2] PASSWORD: ' + l_p)
                    print('Host Name: ' + host_name)
                    print('Local IPS: ' + host_ip)
                    print(
                        '_____________________________________________________________________________________')
                    print('1 for editing user name')
                    print('2 for editing password')
                    edit_b = input('Enter [?] to change settings: ')
                    if edit_b == '1':
                        edit_n = input('Enter new User name: ')
                        with open('user/username.txt', 'w') as f:
                            f.writelines(edit_n)
                            print('User name changed to: ' + edit_n)
                            input('Press enter to close window: ')

                    if edit_b == '2':
                        edit_p = input('Enter new Password: ')
                        with open('user/password.txt', 'w') as f:
                            f.writelines(edit_p)
                            print('Password changed to: ' + edit_p)
                            input('Press enter to close window: ')

                else:
                    print('Wrong password To ' + l_n)

                break

        case '5':
            os.startfile('task.py')

        case '6':
            os.startfile('Telegram Desktop.lnk')

        case '7':
            os.startfile('Корзина.lnk')

        case '8':
            os.startfile('Почта.lnk')
        case '9':
            os.startfile('Hyper.lnk')

        case '10':
            os.startfile('txt.py')

        case '11':
            f = open("demofile.txt", "r")
            print(f.read())

        case 'exit':
            break
