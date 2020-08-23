import pygame
pygame.init()

promt = """Willkommen beim Login"""


def fileAppend(file = "", text = ""):
    with open(file, 'a') as file:
        file.write(text+ '\n')


def makeNewFile(name, text = ''):
    newfile = open(name, 'w+')
    newfile.write(text)


def checkAcc(url = "", file = ""):
    with open(file, 'r') as file:
        lines = file.readlines()
        things = ''
        for line in lines:
            things += line
        if url in things:
            return True
        else:
            return False


#Main Loop
run = True
while run:
    print('\n'+promt)
    answer = input('Neuer Account (1) oder Einloggen (2): ')

    if answer == str(1):
        newName = input('\nErstellen sie einen Benutzernamen: ')
        newPsw = input('Erstellen sie ein Passwort: ')
        newAcc = newName + newPsw
        fileAppend('test', newAcc)
        print('Konto erfolgreich erstellt!')
        continue

    elif answer == str(2):
        name = input('\nGeben sie bitte ihren Benutzernamen ein: ')
        psw = input('Geben sie bitte ihr Passwort ein: ')
        url = name + psw
        bool = checkAcc(url, 'test')
        if bool == True:
            print("Erfolgreich eingeloggt!")
            print('\nDanke fürs Teilnehmen, dies ist leider nur der Login Prozess, also schicke ich sie zurück zum anfang!')
            pygame.time.delay(7000)
            continue
        else:
            print('Falscher Benutzername oder Passwort.')
            continue

    else:
        continue
