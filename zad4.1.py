class TextEditor:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def execute_command(self, command, content=""):
        self.redo_stack.clear()
        
        if command == "ADD":
            old_text = self.text
            self.text += content
            self.undo_stack.append(("ADD", old_text))
        
        elif command == "DELETE":
            if len(self.text) > 0:
                old_text = self.text
                self.text = self.text[:-1]
                self.undo_stack.append(("DELETE", old_text))
        
        elif command == "CLEAR":
            if self.text:
                old_text = self.text
                self.text = ""
                self.undo_stack.append(("CLEAR", old_text))

    def undo(self):
        if not self.undo_stack:
            return False
        
        command, old_text = self.undo_stack.pop()
        self.redo_stack.append((command, self.text))
        self.text = old_text
        return True

    def redo(self):
        if not self.redo_stack:
            return False
        
        command, new_text = self.redo_stack.pop()
        self.undo_stack.append((command, self.text))
        self.text = new_text
        return True

    def get_text(self):
        """Zwraca aktualny tekst"""
        return self.text

def main():
    editor = TextEditor()
    
    while True:
        print("\nAktualny tekst:", editor.get_text())
        print("\nDostępne polecenia:")
        print("1. ADD <tekst> - dodaj tekst")
        print("2. DELETE - usuń ostatni znak")
        print("3. CLEAR - wyczyść tekst")
        print("4. UNDO - cofnij ostatnią operację")
        print("5. REDO - ponów cofniętą operację")
        print("6. EXIT - zakończ program")
        
        command = input("\nWprowadź polecenie: ").strip().split()
        
        if not command:
            continue
            
        if command[0] == "ADD" or command[0] == "add" or command[0] == "Add" and len(command) > 1:
            editor.execute_command("ADD", " ".join(command[1:]))
        elif command[0] == "DELETE" or command[0] == "delete" or command[0] == "Delete":
            editor.execute_command("DELETE")
        elif command[0] == "CLEAR" or command[0] == "clear" or command[0] == "Clear":
            editor.execute_command("CLEAR")
        elif command[0] == "UNDO" or command[0] == "undo" or command[0] == "Undo":
            if not editor.undo():
                print("Brak operacji do cofnięcia!")
        elif command[0] == "REDO" or command[0] == "redo" or command[0] == "Redo":
            if not editor.redo():
                print("Brak operacji do ponowienia!")
        elif command[0] == "EXIT" or command[0] == "exit" or command[0] == "Exit":
            break
        else:
            print("Nieznane polecenie!")

if __name__ == "__main__":
    main()