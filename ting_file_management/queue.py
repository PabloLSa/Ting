class Queue:
    def __init__(self):
        self.itens = []

    def __len__(self):
        return len(self.itens)

    def is_empty(self):
        return len(self.itens) == 0

    def enqueue(self, value):
        self.itens.append(value)

    def dequeue(self):
        if self.is_empty():
            raise KeyError("A fila está vazia, não é possível remover nenhum elemento.")
        return self.itens.pop(0)

    def search(self, index):
        if index < 0 or index >= len(self.itens):
            raise IndexError("Índice Inválido ou Inexistente")
        return self.itens[index]
