def citire():
    '''
    functia citeste lista data
    :return:lista data
    '''
    n=int(input("n="))
    list=[]
    for i in range (n):
        list.append(int(input()))
    return list


def numere_negative(list):
    '''
    functia afiseaza numerele negative nenule din lista
    :param list:lista de numere intregi
    :return:numerele negative nenule din lista
    '''
    sir_negative = []
    for i in range(len(list)):
        if list[i] < 0:
            sir_negative.append(list[i])
    return sir_negative

def test_numere_negative():
    '''
    testeaza daca functia este corecta
    :return:numerele negative din lista
    '''
    assert numere_negative([1, 2, -1, -3]) == [-1, -3]
    assert numere_negative([]) == []
    assert numere_negative([21, -123, 345]) == [-123]

def ultima_cifra_egala_cu_o_cifra_citita(list, x):
    '''
    functia afiseaza cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură
    :param list:lista de numere intregi
    :return:cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură
    '''
    min = 99999999
    for i in range(len(list)):
        if list[i] % 10 == x and list[i] < min:
            min = list[i]
    return min

def test_ultima_cifra_egala_cu_o_cifra_citita():
    '''
    testeaza daca functia este corecta
    :return:cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură
    '''
    assert ultima_cifra_egala_cu_o_cifra_citita([2, 5, 48, 78], 8) == 48
    assert ultima_cifra_egala_cu_o_cifra_citita([], 6) == None
    assert ultima_cifra_egala_cu_o_cifra_citita([458, 355, 665], 5) == 355


def is_prime(n):
    '''
    verifica daca numarul este prim
    :param n: numar natural
    :return: adevarat sau fals
    '''
    if n<2:
        return False
    else:
        ok=True
        for i in range(2, n//2 + 1):
            if n%i == 0:
                ok=False
    if ok:
        return True
    else:
        return False


def superprim(list):
    '''
    functia afiseaza numerele din lista care sunt strict poztive si toate prefixele sale sunt prime
    :param list:lista de numere intregi
    :return:numerele din lista care sunt strict poztive si toate prefixele sale sunt prime
    '''
    sir_superprim = []
    for i in range(len(list)):
        if list[i] > 0:
            p = list[i]
            ok = 1
            while p > 0:
                if is_prime(p) == False:
                    ok = 0
                p = p // 10
            if ok == 1:
                sir_superprim.append(list[i])
    return sir_superprim


def test_superprim():
    '''
    testeaza daca functia este corecta
    :return:numerele din lista care sunt strict poztive si toate prefixele sale sunt prime
    '''
    assert superprim([123, 239, 235]) == [239, 235]
    assert superprim([122, 224, 44]) == []
    assert superprim([333, 22222, 232]) == [333, 22222, 232]


def CMMDC(x, y):
    '''
    functia calculeaza cmmdc al lor
    :param x:numar intreg
    :param y:numar intreg
    :return:cmmdc al lor
    '''
    while x != y:
        if x > y:
            x = x-y
        else:
            y = y-x
    return x


def lista_obtinuta(list):
    '''
    functia afiseaza lista obținuta din lista inițială în care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă
    :param list:lista de numere intregi
    :return:lista obținuta din lista inițială în care numerele pozitive și nenule au fost înlocuite cu CMMDC-ul lor și numerele negative au cifrele în ordine inversă
    '''

def menu():
    print("Alegeti optiunea:")
    print("1.Citire")
    print("2.Afisare numere negative")
    print("3.Afisare cel mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură")
    print("4.Afiseaza numerele din lista care sunt strict poztive si toate prefixele sale sunt prime")
    print("5.Lista obtinuta")
    print("0.Iesire")


def main():
    list = []
    menu()
    option = int(input("Option="))
    while option != 0:
        if option == 1:
            list=citire()
        elif option == 2:
            print(numere_negative(list))
        elif option == 3:
            x = int(input("x="))
            print(ultima_cifra_egala_cu_o_cifra_citita(list, x))
        elif option == 4:
            print(superprim(list))
        elif option == 5:
            print(lista_obtinuta(list))
        elif option == 0:
            break
        menu()
        option = int(input("Option="))



if __name__ == '__main__':
    main()

