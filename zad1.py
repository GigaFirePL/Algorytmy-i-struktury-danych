import time

def algorytm_staly(n):
    kroki = 0
    kroki += 1
    return kroki

def algorytm_liniowy(n):
    kroki = 0
    for i in range(n):
        kroki += 1
    return kroki

def algorytm_kwadratowy(n):
    kroki = 0
    for i in range(n):
        for j in range(n):
            kroki += 1
    return kroki

def algorytm_wykladniczy(n):
    kroki = 0
    def funkcja_rekurencyjna(n):
        nonlocal kroki
        if n <= 0:
            kroki += 1
            return
        kroki += 1
        funkcja_rekurencyjna(n-1)
        funkcja_rekurencyjna(n-1)
    funkcja_rekurencyjna(n)
    return kroki

def zmierz_algorytm(algorytm, n):
    czas_start = time.time()
    kroki = algorytm(n)
    czas_koniec = time.time()
    return kroki, czas_koniec - czas_start

rozmiary = [100, 10000, 1000000]

print("Algorytm Stały:")
for rozmiar in rozmiary:
    kroki, czas = zmierz_algorytm(algorytm_staly, rozmiar)
    print(f"n={rozmiar}, kroki={kroki}, czas={czas:.4f} sekund")

print("\nAlgorytm Liniowy:")
for rozmiar in rozmiary:
    kroki, czas = zmierz_algorytm(algorytm_liniowy, rozmiar)
    print(f"n={rozmiar}, kroki={kroki}, czas={czas:.4f} sekund")
    
rozmiary = [100, 1000, 10000]

print("\nAlgorytm Kwadratowy:")
for rozmiar in rozmiary:
    kroki, czas = zmierz_algorytm(algorytm_kwadratowy, rozmiar)
    print(f"n={rozmiar}, kroki={kroki}, czas={czas:.4f} sekund")

rozmiary = [10, 20, 25]

print("\nAlgorytm Wykładniczy:")
for rozmiar in rozmiary:
        kroki, czas = zmierz_algorytm(algorytm_wykladniczy, rozmiar)
        print(f"n={rozmiar}, kroki={kroki}, czas={czas:.4f} sekund")
