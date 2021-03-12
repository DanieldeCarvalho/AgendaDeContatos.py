CONTACTS = {}

def search_contact(contact):
    try:
        print('Name:', contact)
        print('Telephone:', CONTACTS[contact]['telephone'])
        print('Email:', CONTACTS[contact]['email'])
        print('Adress:', CONTACTS[contact]['address'])
        print("-----------------------")
    except KeyError:
        print()
        print(">>>>>>  Oops!  That was no valid name.  Try again...")
        print()
    except Exception as error:
        print('>>>>>> an unexpected error has occurred')
        print(error)


def show_all_contacts():
    if CONTACTS:  # verifica se CONTACTS existe. evita erro de logica caso CONTACTS não exista
        for contact in CONTACTS:
            print("-----------------------")
            search_contact(contact)
    else:
        print('>>>>>  There is no contact book!')


def read_contact():
    telephone = input("Enter a contact telephone: ")
    email = input("Enter a contact email: ")
    address = input("Enter a contact address: ")
    return telephone, email, address


def add_edit_contact(contact, telephone, email, address):
    CONTACTS[contact] = dict(telephone=telephone, email=email, address=address)  # usei dict constructor
    save_contacts()

def delete_contact(name):
    try:
        CONTACTS.pop(name)
        save_contacts()
        print()
        print(f">>>>>>  Contact {name} was successfully deleted! ")
        print()
    except:
        print(">>>>>>  Invalid contact!")


#add_edit_contact('Joana', '912903190', None, None)


def export_contacts(file_name):
    try:
        with open(file_name, 'w') as file:
            for contact in CONTACTS:
                telephone = CONTACTS[contact]['telephone']
                email = CONTACTS[contact]['email']
                address = CONTACTS[contact]['address']
                file.write(f'{contact},{telephone},{email},{address}\n')

            print('>>>>> Contact book successfully exported')
    except Exception as error:
        print(error)
        print('>>>>> An unexpected error has occurred')
    pass


def import_contacts(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines() #retorna uma lista e .readline() transforma numa string
            for line in lines:
                details = line.strip().split(',') #strip tira o \n do final da string split transforma a string numa lista separando ela com o parametro passado, nesse caso a cima foi a virgula
                name = details[0]
                telephone = details[1]
                email = details[2]
                address = details[3]
                add_edit_contact(name, telephone, address, email)
                print(f'>>>>> contact {name} added successfully!')
    except FileNotFoundError:
        print('>>>>> File not found')
    except Exception as error:
        print(error)
        print('>>>>> An unexpected error has occurred')


def save_contacts():
    export_contacts('database.csv')


def load():
    try:
        with open('database.csv', 'r') as file:
            lines = file.readlines()  # retorna uma lista e .readline() transforma numa string
            for line in lines:
                details = line.strip().split(
                    ',')  # strip tira o \n do final da string split transforma a string numa lista separando ela com o parametro passado, nesse caso a cima foi a virgula
                name = details[0]
                telephone = details[1]
                email = details[2]
                address = details[3]

                CONTACTS[name] = dict(telephone=telephone, email=email, address=address)

            print(f'>>>>> Database loaded successfully')
            print(f'>>>>> {len(CONTACTS)} contacts loaded!')
    except FileNotFoundError:
        print('>>>>> File not found')
    except Exception as error:
        print(error)
        print('>>>>> An unexpected error has occurred')


def show_menu():
    print("-----------------------")
    print('1 - Show all contacts')
    print('2 - Search contact')
    print('3 - Add contact')
    print('4 - Edit contact')
    print('5 - delete contact')
    print('6 - Export contacts for CSV')
    print('7 - Import contacts from CSV')
    print('0 - Close contact book')
    print("-----------------------")

#inicio do programa
load()

while True:
    show_menu()
    option = input('Choose an option: ')
    if option == "1":
        show_all_contacts()

    elif option == "2":
        contact = input("Enter a contact name: ")
        search_contact(contact)

    elif option == "3":
        contact = input("Enter a contact name: ")
        try:
            CONTACTS[contact]  # verifica se o contato existe.
            print('>>>>>  Contact already exists!')
        except:
            telephone, email, address = read_contact() # nao importa o nome, apenas a ordem aqui eu uso a
            # ordem que determinei no return da função
            print('>>>>>  Adding contact ', contact)
            add_edit_contact(contact, telephone, email, address)
            print(f">>>>>>  Contact {contact} has been successfully added! ")

    elif option == "4":
        contact = input("Enter a contact name: ")
        try:
            CONTACTS[contact]  # verifica se o contato existe.
            print('>>>>>  Editing contact!')
            telephone, email, address = read_contact()
            add_edit_contact(contact, telephone, email, address)
            print(f">>>>>>  Contact {contact} has been successfully edited! ")
        except:
            print('>>>>>  Contact does not exists!')
            pass

    elif option == "5":
        contact = input("Enter a contact name: ")
        delete_contact(contact)

    elif option == "6":
        file_name = input('Enter the file name: ')
        export_contacts(file_name)

    elif option == "7":
        file_name = input('Enter the file name: ')
        import_contacts(file_name)

    elif option == "0":
        print(">>>>>>  Closing the program!")
        break

    else:
        print('>>>>>>  Invalid option')
