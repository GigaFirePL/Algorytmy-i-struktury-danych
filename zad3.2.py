class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.steps = 0

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def drzewo(self, prefix):
        self.steps = 0
        node = self.root
        for char in prefix:
            self.steps += 1
            if char not in node.children:
                return []
            node = node.children[char] #Złożoność czasowa: O(p + k), gdzie p - długość prefiksu k - liczba znalezionych słów Złożoność pamięciowa: O(n * m), gdzie: n - liczba słów m - średnia długość słowa
        
        words = []
        self._collect_words(node, prefix, words)
        return words, self.steps

    def _collect_words(self, node, prefix, words):
        if node.is_end:
            words.append(prefix)
        
        for char, child in node.children.items():
            self.steps += 1
            self._collect_words(child, prefix + char, words)

def tablica(words, prefix):
    steps = 0
    result = []
    for word in words:
        steps += 1
        if word.startswith(prefix):
            result.append(word)
    return result, steps #Złożoność czasowa: O(n*m), pamięciowa: O(1), gdzie n to liczba słów, a m to długość prefiksu

slowa = [
    "auto", "akacja", "ananas", "apteka", "arbuz", "atlas",
    "bank", "basen", "bomba", "butla", "biurko", "balkon",
    "chleb", "ciasto", "czapka", "cześć", "czajnik", "cebula",
    "dach", "deska", "dobro", "droga", "drzewo", "dudek",
    "ekran", "etyka", "energia", "epoka", "ekipa", "elder",
    "fala", "figura", "foka", "farba", "frytki", "fasola",
    "gracz", "gazeta", "godzina", "granica", "grzyb", "głowa",
    "hotel", "hamak", "herbata", "historia", "humor", "hałas",
    "igła", "ikona", "iskra", "imię", "irys", "idol",
    "jabłko", "jajko", "jazda", "jeleń", "język", "jogurt",
    "kawa", "klucz", "komputer", "kot", "krzesło", "książka",
    "lampa", "lato", "liść", "lodówka", "lustro", "lalka",
    "mama", "mapa", "masło", "medal", "miasto", "mleko",
    "noga", "nora", "notes", "natura", "niebo", "nożyce",
    "obraz", "ogród", "okno", "olej", "orzeł", "owoc",
    "papa", "pies", "pilot", "pizza", "pralka", "praca",
    "radio", "rama", "rower", "ręka", "rzeka", "ryba",
    "sala", "serce", "sklep", "słoń", "smok", "sowa",
    "tata", "taras", "telefon", "torba", "trawa", "troll",
    "ulica", "ucho", "urna", "układ", "umowa", "uśmiech",
    "woda", "wiatr", "wilk", "wąż", "węgiel", "wyspa",
    "zegar", "zima", "zamek", "zebra", "zupa", "złoto"
]

if __name__ == "__main__":
    trie = Trie()
    for word in slowa:
        trie.insert(word)

    prefix = "z"
    
    array_results, array_steps = tablica(slowa, prefix)
    print(f"\nWyszukiwanie w tablicy dla prefiksu '{prefix}':")
    print(f"Znalezione słowa: {array_results}")
    print(f"Liczba kroków: {array_steps}")
    
    trie_results, trie_steps = trie.drzewo(prefix)
    print(f"\nWyszukiwanie w drzewie trie dla prefiksu '{prefix}':")
    print(f"Znalezione słowa: {trie_results}")
    print(f"Liczba kroków: {trie_steps}")