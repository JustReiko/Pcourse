def greeting():
    print('Greetings! \n')

def menu():
    print('Phonebook\n***********************\n**Choose an action**\n 1. Search phone book\n 2. Add a record\n 3. View contacts\n 4. Change a record\n')


def show_phonebook():
    path = 'file.txt'
    file = open(path, 'r', 'utf-8')
    for line in file:
        print(line)
    file.close()
