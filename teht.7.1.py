vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
while True:
    if kuukauden_numero == 12 or (kuukauden_numero == 1) or (kuukauden_numero == 2):
        print(vuodenajat[0])
        kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
    elif kuukauden_numero == 3 or (kuukauden_numero == 4) or (kuukauden_numero == 5):
        print(vuodenajat[1])
        kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
    elif kuukauden_numero == 6 or (kuukauden_numero == 7) or (kuukauden_numero == 8):
        print(vuodenajat[2])
        kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
    elif kuukauden_numero == 9 or (kuukauden_numero == 10) or (kuukauden_numero == 11):
        print(vuodenajat[3])
        kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
