def sprawdz_palindrom(str):
    list1 = []
    list2 = []
    backwards = ''

    for letter in str:
        list1.append(letter)

    print(list1)

    for letter in reversed(list1):
        list2.append(letter)
    
    print(list2)

    backwards = ''.join(list2)

    print(backwards)

    #if str == list2:
    #    return(True)
    #else
    #    return(False)

print('wprowadź wyraz:')
wyraz = input()
sprawdz_palindrom(wyraz)
