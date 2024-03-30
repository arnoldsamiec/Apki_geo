
#6
dane = (2024, 'Python', 3.8)

#print(dane)
(rok, język, wersja) = dane

#print(rok)
#print(język)
#print(wersja)

#7
oceny = [4, 3, 5, 2, 5, 4]

pierwsza, *srodek, ostatnia = oceny

#print("Pierwsza:", pierwsza)
#print("Ostatnia:", ostatnia)
#print("Środkowe:", srodek)

#8
info = ('Jan', 'Kowalski', 30, 'Polska', 'programista')

imie, nazwisko, *_, zawod = info

#print(imie)
#print(nazwisko)
#print(zawod)

#9
dane = (2024, ['Python', 3.8, ('Stabilna', 'Wersja')])

rok, (jezyk, wersja, opis) = dane

#print("Rok:", rok)
#print("Nazwa języka:", jezyk)
#print("Wersja:", wersja)
#print("Opis wersji:", opis)

#10
a = b = [1, 2, 3]
b[0] = 'zmieniono'


#11
c = a[:]
c[0] = 'nowa wartość'
print(a)
print(b)
print(c)

#12
x = y = 10
y = y+1

print(x)
print(y)

#13
K = [1, 2]
L = K
print(K,L)
K = K + [3, 4]
print(K,L)
M = [1, 2]
N = M
print(M,N)
M += [3, 4]
print(M,N)
#k i l tworzy kopie, natomiast m i n dopisuja wciaz do tej samej zmiennej

#14
imiona = ['Anna', 'Jan', 'Ewa']
oceny = [5, 4, 3]

for imie, ocena in zip(imiona, oceny):
    print(f"Imię: {imie}, Ocena: {ocena}")
#Jeśli listy mają rozne długości,
#to funkcja zip() połączy tylko tyle elementów ile ma krótsza lista

#15
def kwadrat(x):
    return x ** 2

liczby = [1, 2, 3, 4, 5]

nowa_lista = list(map(kwadrat, liczby))

print(nowa_lista)

#16
def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = 'kalafior'
    elif isinstance(arg, int):
        arg = 65482652

test_lista = ['marchew', 1, 2, 3]

zmien_wartosc(test_lista)
print(test_lista)

test_numer = 4353

zmien_wartosc(test_numer)
print(test_numer)

#17

def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    zamowienie = {
        'nazwa_produktu': nazwa_produktu,
        'cena': cena,
        'ilosc': ilosc,
        'suma': cena * ilosc
    }
    return zamowienie, cena * ilosc

zamowienia = []

#19

def stworz_funkcje_potegujaca(wykladnik):
    def poteguj(podstawa):
        return podstawa ** wykladnik
    return poteguj

potega = stworz_funkcje_potegujaca(3)
print(potega(2)) # Wynik: 8

#20
#AAAAAAAAAAAAAAAA
def licznik():
    counter = 0
    def nested_licznik():
        nonlocal counter
        counter += 1
        return counter
    return nested_licznik

licznik_a = licznik()
print(licznik_a())
print(licznik_a())
print(licznik_a()) 

#BBBBBBBBBBBBBBBBb

counter = 0

def licznik():
    global counter
    counter += 1
    return counter

print(licznik())
print(licznik())
print(licznik())

#CCCCCCCCCCCCCCCCC

class Licznik:
    def __init__(self):
        self.counter = 0

    def __call__(self):
        self.counter += 1
        return self.counter

licznik_c = Licznik()
print(licznik_c())
print(licznik_c())
print(licznik_c()) 

#DDDDDDDDDDDDDDDDDDD

def licznik():
    if not hasattr(licznik, 'counter'):
        licznik.counter = 0
    licznik.counter += 1
    return licznik.counter

print(licznik())  # Output: 1
print(licznik())  # Output: 2
print(licznik())  # Output: 3

#21

def str_wrapper(obj: object) -> str:
    
    return str(obj)

number = 1234
text_number = str_wrapper(number)
print(text_number)  # '1234'
print(type(text_number))  # <class 'str'>

#22

books = [
    {'tytul': 'Book 1', 'autor': 'Author 1', 'rok_wydania': 2005},
    {'tytul': 'Book 2', 'autor': 'Author 2', 'rok_wydania': 2000},
    {'tytul': 'Book 3', 'autor': 'Author 3', 'rok_wydania': 2010},
    {'tytul': 'Book 3', 'autor': 'Author 3', 'rok_wydania': 2007},
    {'tytul': 'Book 3', 'autor': 'Author 3', 'rok_wydania': 1996}
]

sorted_books = sorted(books, key=lambda book: book['rok_wydania'])

print(sorted_books)

filtered_books = list(filter(lambda book: book['rok_wydania'] > 2000, books))
print(filtered_books)

title_list = list(map(lambda book: book['tytul'], books))

print(title_list)

#23

def days_of_week():
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day in days:
        yield day

days_generator = days_of_week()

for day in days_generator:
    print(day)

days_generator = days_of_week()
first_three_days = []

try:
    for _ in range(3):
        first_three_days.append(next(days_generator))
except StopIteration:
    pass

print(first_three_days)


