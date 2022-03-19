class Contact:

    def __init__(self,name,phone,email) :
        self._name = name
        self._phone = phone
        self._email = email

class ContactBook:
    def _init_(self):
        self._contacts = []
    
    def add(self, name, phone, email):
        print('name:{},phone:{}, email:{}'.format(name,phone,email)) 

def run():

    contact_book = ContactBook()
    while True:
        command = str(input(
            '''
            [a] añadir 
            [ac] actualizar 
            [b] buscar
            [e] eliminar
            [l] listar
            [s] salir
            '''
        ))

        if command == 'a':
            name = str(input('Escribe el nomre del contacto;'))
            phone = str(input('Escribe el  telefono:'))
            email = str(input('Escribe el email'))

            contact_book.add(name, phone, email)

if __name__ == '_main_':
    run()