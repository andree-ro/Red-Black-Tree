from nodo import RBN
from tree_BR import RBT
from os import system

rbt = RBT()

while True:
    system('cls')
    choice = input('Menu\n1. Insertar números\n2. Imprimir PreOrder\n3. Imprimir números con su color\n4. Salir\n')

    if choice == '1':
        system('cls')

        numbers = input('Inserte la cadena de números que desea agregar al árbol: ')
        split_numbers = numbers.split()

        for x in split_numbers:
            rbt.add(RBN(int(x)))

    elif choice == '2':
        system('cls')

        print(rbt.traverse())

        system('pause')

    elif choice == '3':
        system('cls')

        print(rbt.midTraverse(rbt.root))

        system('pause')

    elif choice == '4':
        system('cls')

        break
