def sprawdz_palindrom(str):
    """
        sprawdza czy wpisany wyraz jest palindromem
        zwraca wartość boolean True jeśli jest, False jest nie jest
    """    
    backwards = str[::-1]
    
    return (str == backwards)

print('wprowadź wyraz:')
wyraz = input()
sprawdz_palindrom(wyraz)
