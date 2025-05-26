from collections import deque

def flood_fill_dfs(image, sr, sc, new_color):
    """
    Implementacja algorytmu Flood Fill używając rekurencyjnego DFS
    Złożoność czasowa: O(n*m)
    Złożoność pamięciowa: O(n*m)
    """
    rows, cols = len(image), len(image[0])
    old_color = image[sr][sc]
    
    if old_color == new_color:
        return image
    
    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            image[r][c] != old_color):
            return
        
        image[r][c] = new_color
        
        # 4-kierunkowe sąsiedztwo
        dfs(r+1, c)  # dół
        dfs(r-1, c)  # góra
        dfs(r, c+1)  # prawo
        dfs(r, c-1)  # lewo
    
    dfs(sr, sc)
    return image

def flood_fill_bfs(image, sr, sc, new_color):
    """
    Implementacja algorytmu Flood Fill używając iteracyjnego BFS
    Złożoność czasowa: O(n*m)
    Złożoność pamięciowa: O(n*m)
    """
    rows, cols = len(image), len(image[0])
    old_color = image[sr][sc]
    
    if old_color == new_color:
        return image
    
    queue = deque([(sr, sc)])
    
    while queue:
        r, c = queue.popleft()
        if (r < 0 or r >= rows or c < 0 or c >= cols or 
            image[r][c] != old_color):
            continue
            
        image[r][c] = new_color
        
        # 4-kierunkowe sąsiedztwo
        neighbors = [
            (r+1, c),  # dół
            (r-1, c),  # góra
            (r, c+1),  # prawo
            (r, c-1)   # lewo
        ]
        
        queue.extend(neighbors)
    
    return image

def print_image(image):
    """Wyświetla obraz w czytelnej formie"""
    for row in image:
        print(' '.join(map(str, row)))

def main():
    # Test dla obu algorytmów
    image = [
        [1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    
    # Test DFS
    print("orginał:")
    print_image(image)
    
    image_dfs = [row[:] for row in image]  # Kopia obrazu
    sr, sc = 1, 1  # Punkt startowy
    new_color = 2  # Nowy kolor
    
    print("\nrekurencyjne DFS (start: ({}, {}), nowy kolor: {}):".format(sr, sc, new_color)) 
    flood_fill_dfs(image_dfs, sr, sc, new_color) 
    print_image(image_dfs) 
    
    # Test BFS
    image_bfs = [row[:] for row in image]  # Kopia obrazu
    
    print("\niteracyjny BFS (start: ({}, {}), nowy kolor: {}):".format(sr, sc, new_color))
    flood_fill_bfs(image_bfs, sr, sc, new_color) 
    print_image(image_bfs)

if __name__ == "__main__":
    main()