class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size

    def insert(self, data):

        self.insertAT(self.size, data)

    def insertAT(self, position, data):

        if position < 0 or position > self.size:
            print(f"[erro] posição {position} inválida (tamanho atual: {self.size})")
            return False

        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1
        return True
    def removeAT(self, position):

        if self.is_empty():
            print("[erro] lista vazia, nada para remover")
            return None 
        
        if position < 0 or position >= self.size:
            print(f"[erro] posição {position} inválida (tamanho atual: {self.size})")
            return None

        if position == 0:
            removed = self.head
            self.head = self.head.next
        else:
    
            current = self.head
            for _ in range(position - 1):
                current = current.next
            removed = current.next
    
            current.next = removed.next

        self.size -= 1
        removed.next = None  
        return removed.data

    def remove_by_value(self, value):
       
        current = self.head
        position = 0
        while current:
            if current.data.lower() == value.lower():
                return self.removeAT(position)
            current = current.next
            position += 1
        return None

    def to_list(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items
    
    def clear(self):
        self.head = None
        self.size = 0

class ShoppingListApp:
    
    def __init__(self):
        self.compras = LinkedList()

    def run(self):
        print("=== Lista de Compras (lista encadeada) ===")
        print(self.COMMANDS)
        while True:
            entrada = input(">> ").strip()
            if not entrada:
                continue

            partes = entrada.split(maxsplit=2)
            comando = partes[0].lower()

            if comando == "sair":
                print("Até mais!")
                break

            elif comando == "help":
                print(self.COMMANDS)

            elif comando == "add" and len(partes) >= 2:
                item = entrada[len(comando):].strip()
                self.compras.insert(item)
                print(f"'{item}' adicionado.")

            elif comando == "insert" and len(partes) >= 3:
                try:
                    pos = int(partes[1])
                except ValueError:
                    print("[erro] posição deve ser um número inteiro")
                    continue
                item = partes[2]
                self.compras.insertAT(pos, item)

            elif comando == "remove" and len(partes) >= 2:
                try:
                    pos = int(partes[1])
                except ValueError:
                    print("[erro] posição deve ser um número inteiro")
                    continue
                removido = self.compras.removeAT(pos)
                if removido is not None:
                    print(f"'{removido}' removido.")

            elif comando == "removenome" and len(partes) >= 2:
                item = entrada[len(comando):].strip()
                removido = self.compras.remove_by_value(item)
                if removido is not None:
                    print(f"'{removido}' removido.")
                else:
                    print(f"'{item}' não encontrado na lista.")

            elif comando == "clear":
                self.compras.clear()
                print("Lista limpa.")

            elif comando == "list":
                self._mostrar_lista()

            else:
                print("Comando não reconhecido. Digite 'help' para ver os comandos.")

    def _mostrar_lista(self):
        itens = self.compras.to_list()
        if not itens:
            print("(lista de compras vazia)")
            return
        print("Lista de compras:")
        for i, item in enumerate(itens):
            print(f"  [{i}] {item}")


if __name__ == "__main__":
    app = ShoppingListApp()
    app.run()