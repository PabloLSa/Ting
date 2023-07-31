class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("A fila está vazia, não é possível remover nenhum elemento.")
        return self.items.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.items):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.items[index]

    def is_empty(self):
        return len(self.items) == 0
