"""ZADATAK 2 - provjeriti da li je rijec palindrom, ako je vrati True, ako nije vrati False. Provjeri da li je ulazni parametar string"""

def je_palindrom(rijec):
    """
    Provjerava je li dana rijec palindrom.
    :param rijec: rijec koja se provjerava
    :return: True ako je palindrom else False
    """
    # Provjera je li ulazni parametar string
    if not isinstance(rijec, str):
        raise ValueError("Ulazni parametar mora biti string.")
    
    # Provjera je li rijec palindrom
    rijec = rijec.replace(" ", "").lower()
    return rijec == rijec[::-1]

#print(je_palindrom("madam"))

try:
    #print(je_palindrom(1234))
    print(je_palindrom("level"))
    #print(je_palindrom("house"))
except ValueError as e:
    print(f"Greška: {e}")