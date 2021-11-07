import random
from math import gcd as gcd


def phi(n):
    result = 1
    for i in range(2, n):
        if gcd(i, n) == 1:
            result += 1
    return result


def generate_list_of_numbers(n):
    list = []
    for i in range(1, n):
        if gcd(i, n) == 1:
            list.append(i)
    return list


def modular_multiplication(a, b, n):
    return (a * b) % n


def prime_factors(n):
    list = []
    while n % 2 == 0:
        list.append(2)
        n = n / 2
    import math

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            list.append(int(i))
            n = n / i
    if n > 2:
        list.append(int(n))
    return list


def remove_duplicates_from_list(list):
    output = []
    for i in list:
        if i not in output:
            output.append(i)
    return output


def test_pierwszosci_Lucasa(n):
    n1 = n - 1
    b = 2
    podzielniki = remove_duplicates_from_list(prime_factors(n1))
    while b < n:
        bool = True
        for p in podzielniki:
            if pow(b, n1, n) == 1 and pow(b, int(n1 / p), n) != 1:
                continue
            else:
                bool = False
                break
        if bool:
            return True
        b = b + 1
    return False


def oblicz_rząd_elementu_w_grupie(element, modulo):
    i = element
    rząd = 1
    list = []
    while i != 1:
        i = modular_multiplication(i, element, modulo)
        list.append(i)
        if len(list) != len(set(list)):
            return "nieskończoność"
        rząd = rząd + 1
    return rząd


def znajdz_pierwiastek_pierwotny(modulo):
    rząd = len(generate_list_of_numbers(modulo))
    pierwiastki = []
    for element in generate_list_of_numbers(modulo):
        if oblicz_rząd_elementu_w_grupie(element, modulo) == rząd:
            pierwiastki.append(element)
    return pierwiastki


def znajdz_element_odwrotny(element, modulo):
    list = generate_list_of_numbers(modulo)
    for number in list:
        if modular_multiplication(element, number, modulo) == 1:
            return number
    return "Brak elementu odwrotnego"


print("Zadanie pierwsze:")
print("n=19")
for element in generate_list_of_numbers(19):
    print(
        "Element "
        + str(element)
        + ", rząd: "
        + str(oblicz_rząd_elementu_w_grupie(element, 19))
    )

print("n=24")
for element in generate_list_of_numbers(24):
    print(
        "Element "
        + str(element)
        + ", rząd: "
        + str(oblicz_rząd_elementu_w_grupie(element, 24))
    )

print("\nZadanie drugie:")
print("Pierwiastki pierwotny")
print("-w grupie multiplikatywnej n=19: " + str(znajdz_pierwiastek_pierwotny(19)))
print("-w grupie multiplikatywnej n=41: " + str(znajdz_pierwiastek_pierwotny(41)))

print("\nZadanie trzecie:")
n = pow(2, 8)
list = generate_list_of_numbers(n)
phin = phi(n)
exists = False
for element in list:
    if oblicz_rząd_elementu_w_grupie(element, n) == phin:
        exists = True
        break
print("W grupie multiplikatywnej o n=2^8 pierwiastek pierwotny:")
if exists:
    print("istnieje.")
else:
    print("nie istnieje.")
# TODO: trzeba sprawdzić czy snieje takie n>=3 ...

print("\nZadanie czwarte:")
print("W grupie multiplikatywnej n=19:")
for element in generate_list_of_numbers(19):
    print(
        "Dla elementu "
        + str(element)
        + " elementem odwrotnym jest "
        + str(znajdz_element_odwrotny(element, 19))
    )
print("W grupie multiplikatywnej n=24:")
for element in generate_list_of_numbers(24):
    print(
        "Dla elementu "
        + str(element)
        + " elementem odwrotnym jest "
        + str(znajdz_element_odwrotny(element, 24))
    )

print("\nZadanie piąte:")
print("Test pierwszości Lucasa - liczba i wynik czy liczba jest pierwsza\n")
prime = 3316699487
print(prime)
print(test_pierwszosci_Lucasa(prime))
print()
for i in range(2):
    number = int.from_bytes(random.randbytes(5), "big")
    print(number)
    print(test_pierwszosci_Lucasa(number))
    print()
