znaky = {
        """Morse Script."""
        'A': '.-', 'B': '-...',
        'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-',
        'L': '.-..', 'M': '--', 'N': '-.',
        'O': '---', 'P': '.--.', 'Q': '--.-',
        'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--',
        'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--',
        '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.',
        '0': '-----'
}

def encodovani(vstup):
    """
    Encode.
    Args vstup.
    >>> encodovani('a')
    .-
    """
    zprava = ''
    i = 0
    for znak in vstup.upper():
        if znak != ' ':
            zprava += znaky[znak]
            if len(vstup)-1 != i:
                zprava+= ' '
        i += 1
    return zprava

def decodovani(vstup):
    """
    Decode.
    Args vstup.
    >>> decodovani('.-')
    A
    """
    try:
        vstup += " "
        desifrovanaZprava = ''
        pismeno = ''
        i = 0
        for letter in vstup:
            if (letter != ' '):
                i = 0
                pismeno += letter
            else:
                i += 1
                if i == 2:
                    desifrovanaZprava += ' '
                else:
                    desifrovanaZprava += list(znaky.keys())[list(znaky.values()).index(pismeno)]
                    pismeno = ''
        return desifrovanaZprava
    except ValueError:
        return 0

def vypisZnaku():
    """
    Print approved string of chars in array.
    """
    znakPodporovan=""
    vypisZnaku=""
    for znakPodporovan in znaky:
        vypisZnaku+=znakPodporovan
        
    print(vypisZnaku)

def start():
    """
    Main console function.
    """
    print("Zvolte: 'e' pro encode, 'd' pro decode, jinou klávesu pro ukončení programu:")
    print("Podporované znaky:")
    vypisZnaku()
    
    typ = input()

    if typ=="e":
        print("Zadejte vstup pro encode:")
        vstup = input()
        print("Enkodováno:")
        print(encodovani(vstup))
        
    elif typ=="d":
        print("Zadejte vstup pro decode:")
        vstup = input()

        res = decodovani(vstup)       
        if res!=0:
            print("Dekodováno:")
            print(decodovani(vstup))
        else:
            print("Chyba - Nelze dekódovat.")
            start()

print("Vítejte v encoderu/decoderu pro morseovku")
start()


