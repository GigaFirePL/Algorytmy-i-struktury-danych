from collections import defaultdict

def main():
    # 1. Lista ocen
    grades = [5, 3, 8, 6, 2, 7, 4]

    # 2. Średnia
    avg = sum(grades) / len(grades)
    print("Average:", avg)

    # 3. Filtrowanie <4
    grades = [g for g in grades if g >= 4]
    # grades: [5,8,6,7,4]

    # 4. Odwróć kolejność
    grades.reverse()
    # grades: [4,7,6,8,5]

    # 5. Grupowanie
    cats = defaultdict(list)
    for g in grades:
        key = "low" if g < 4 else ("mid" if g <= 6 else "high")
        cats[key].append(g)

    # 6. Wypisz
    for k, vs in cats.items():
        print(f"{k}: {vs}")

if __name__ == "__main__":
    main()
