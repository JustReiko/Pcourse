import view
import model
def run():
    view.greetings()
    while True:
        view.menu()
        choice = int(input())
        match choice:
            case 1:
                model.search()
            case 2:
                model.add_contact()
            case 3:
                model.view_phonebook()
            case 4:
                model.update()
            case _:
                print('The value is incorrect, try again')
                view.menu()