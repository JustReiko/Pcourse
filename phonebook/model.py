def add_contact():
    first_name = input('Enter your name: ')
    last_name = input('Enter your surname: ')
    phone = input('Enter your phone number: ')
    file = open("file.txt", "a")
    file.write(first_name + ' ')
    file.write(last_name + ' ')
    file.write(phone + '\n')
    file.close()
    pass

def search():
    file = open('file.txt', 'r', 'utf-8')
    f = input("")
    lines = file.readlines()
    lines = view_phonebook()
    cnt = 0
    for line in lines:
        if f in line:
            print(line)
        else:
            print('Contact is not found')

def view_phonebook():
    file = open('file.txt', 'r', 'utf-8')
    lines = file.readlines()
    mat_line = []
    for line in lines:
        mat_line.append(line)
    file.close()
    return mat_line

def update():
    file = open('file.txt', 'w', 'utf-8')
    f = input("")
    lines = file.readlines()
    lines = view_phonebook()
    cnt = 0
    for line in lines:
        if f in line:
            print('Enter new data')
            new = input("")
            f.writelines(new)
            print(line)
        else:
            print('Contact is not found')
    pass

