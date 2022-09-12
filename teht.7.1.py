vuodenajat = ("talvi", "kevät", "kesä", "syksy")
kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
if kuukauden_numero == 12 or 1 or 2:
    print(vuodenajat[0])
    kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
elif kuukauden_numero == 3 or 4 or 5:
    print(vuodenajat[1])
    kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
elif kuukauden_numero == 6 or 7 or 8:
    print(vuodenajat[2])
    kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
elif kuukauden_numero == 9 or 10 or 11:
    print(vuodenajat[3])
    kuukauden_numero = int(input('Anna kuukauden numero (1-12): '))
