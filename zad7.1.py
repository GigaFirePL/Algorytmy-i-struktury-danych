def find_permutations(string):
    """
    Znajduje wszystkie permutacje ciągu znaków używając rekurencji
    Złożoność czasowa: O(n!)
    Złożoność pamięciowa: O(n)
    """
    if len(string) <= 1:
        return [string]
    
    perms = []
    for i, char in enumerate(string):
        # Dla każdego znaku, znajdź permutacje pozostałych znaków
        remaining_chars = string[:i] + string[i+1:]
        for p in find_permutations(remaining_chars):
            perms.append(char + p)
    return perms

def to_binary(n):
    """
    Konwertuje liczbę dziesiętną na binarną używając rekurencji
    Złożoność czasowa: O(log n)
    Złożoność pamięciowa: O(log n)
    """
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return to_binary(n // 2) + str(n % 2)

def find_path(maze, current, end, visited=None):
    """
    Znajduje ścieżkę w labiryncie używając rekurencji i algorytmu DFS
    Złożoność czasowa: O(n*m)
    Złożoność pamięciowa: O(n*m)
    """
    if visited is None:
        visited = set()
    
    rows, cols = len(maze), len(maze[0])
    row, col = current
    
    # Sprawdź warunki brzegowe
    if (row < 0 or row >= rows or 
        col < 0 or col >= cols or 
        maze[row][col] == 1 or 
        (row, col) in visited):
        return None
    
    # Znaleziono cel
    if (row, col) == end:
        return [(row, col)]
    
    # Dodaj obecną pozycję do odwiedzonych
    visited.add((row, col))
    
    # Sprawdź wszystkie możliwe kierunki (góra, prawo, dół, lewo)
    for next_row, next_col in [(row-1, col), (row, col+1), (row+1, col), (row, col-1)]:
        path = find_path(maze, (next_row, next_col), end, visited)
        if path:
            return [(row, col)] + path
    
    return None

def print_maze_with_path(maze, path):
    """Wyświetla labirynt z zaznaczoną ścieżką"""
    if not path:
        print("Nie znaleziono ścieżki!")
        return
    
    path_set = set(path)
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if (i, j) in path_set:
                print("*", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()

def main():
    # Test permutacji
    print("\nTest permutacji:")
    string = "ABC"
    perms = find_permutations(string)
    print(f"Permutacje dla '{string}':")
    for p in perms:
        print(p)

    # Test konwersji binarnej
    print("\nTest konwersji binarnej:")
    numbers = [5, 10, 15, 20]
    for n in numbers:
        binary = to_binary(n)
        print(f"{n} w systemie binarnym: {binary}")

    # Test znajdowania ścieżki w labiryncie
    print("\nTest labiryntu:")
    maze = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    start = (0, 0)
    end = (3, 3)
    
    print("Labirynt:")
    for row in maze:
        print(row)
    
    print("\nŚcieżka (oznaczona gwiazdkami):")
    path = find_path(maze, start, end)
    print_maze_with_path(maze, path)

if __name__ == "__main__":
    main()