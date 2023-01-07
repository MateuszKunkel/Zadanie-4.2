def sprawdz_palindrom(str):
    list1 = []
    backwards = ''

    for letter in str:
        list1.append(letter)

    print(list1)

print('wprowadź wyraz:')
wyraz = input()
sprawdz_palindrom(wyraz)
