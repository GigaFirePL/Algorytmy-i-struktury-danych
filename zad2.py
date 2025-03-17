def przesuń(tablica):
    n = len(tablica)
    wynik = [0] * n
    indeks = 0
    
    for i in range(n):
        if tablica[i] < 0:
            wynik[indeks] = tablica[i]
            indeks += 1
    
    for i in range(n):
        if tablica[i] >= 0:
            wynik[indeks] = tablica[i]
            indeks += 1  
    return wynik

tablica = [1, -2, 3, -4, 5, -6, 7, -8, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]
print("a)")
print("Liczby: ", tablica)
print("Ułożone liczby: ",przesuń(tablica)) 


def znajdź(tablica, n):
    suma_n = n * (n + 1) // 2
    suma_tablica = 0
    
    for liczba in tablica:
        suma_tablica += liczba
    
    brakująca_liczba = suma_n - suma_tablica
    return brakująca_liczba

tablica = [1, 2, 4, 5, 6]
n = 6
print("b)")
print("Liczby: ", tablica)
print("Brakująca liczba: ",znajdź(tablica, n))


def znajdź_duplikaty(tablica):
    n = len(tablica)
    duplikaty = []
    odwiedzone = [False] * (n + 1)
    
    for liczba in tablica:
        if odwiedzone[liczba]:
            duplikaty.append(liczba)
        else:
            odwiedzone[liczba] = True
    return duplikaty

tablica = [1, 2, 3, 4, 2, 5, 6, 3, 7, 8, 9, 9]
print("c)")
print("Liczby: ", tablica)
print("Duplikaty: ",znajdź_duplikaty(tablica))


def obróć_tablicę(tablica):
    n = len(tablica)
    for i in range(n // 2):
        tablica[i], tablica[n - i - 1] = tablica[n - i - 1], tablica[i]
    return tablica

# Przykład użycia
tablica = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("d)")
print("Tablica: ", tablica)
print("Odwrócona tablica ",obróć_tablicę(tablica))