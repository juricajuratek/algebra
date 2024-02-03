def zbroj_samoglasnika(lista):
    """
    Zbroji broj samoglasnika u listi.

    Parameters:
    - lista (list): Lista riječi.

    Returns:
    - int: Ukupan broj samoglasnika u listi.
    """
    samoglasnici = "aeiouAEIOU"
    broj_samoglasnika = 0

    for rijec in lista:
        broj_samoglasnika += sum(1 for slovo in rijec if slovo in samoglasnici)

    return broj_samoglasnika

# Primjer korištenja:
rijeci = ["hello", "world", "python", "programming"]
rezultat = zbroj_samoglasnika(rijeci)

print(f"Ukupan broj samoglasnika u listi: {rezultat}")
