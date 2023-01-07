def sprawdz_palindrom(str):
    """
        sprawdza czy wpisany wyraz jest palindromem
        zwraca wartość boolean True jeśli jest, False jest nie jest
    """    
    list1 = []
    list2 = []
    backwards = ''

    for letter in str:
        list1.append(letter)

    for letter in reversed(list1):
        list2.append(letter)

    backwards = ''.join(list2)

    return (str == backwards)

print('wprowadź wyraz:')
wyraz = input()
sprawdz_palindrom(wyraz)
