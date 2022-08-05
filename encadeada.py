from explorer import MyFileExplorer


class Node:
# constructor
    def __init__(self, data = None, _next=None):
        self.data = data
        self._next = _next

# A Linked List class with a single head node
class LinkedList:
    def __init__(self):
        self.head = None

    # insertion method for the linked list
    def insert(self, data):
        newNode = Node(data)

        if(self.head):
            current = self.head

            while(current._next):
                current = current._next
            current._next = newNode
        else:
            self.head = newNode

    # print method for the linked list
    def printLL(self):
        current = self.head
        text = ""
        while(current):
            text += current.data
            current = current._next

        return text


class AlocacaoEncadeada(MyFileExplorer):
    def __init__(self):
        super().__init__()
        self.alocacao = LinkedList()

    def create_aloc(self, filename):
        with open(filename, "r") as f:
            conteudo = (f.readlines())[0]
            _max = 300

            for i in range(0, _max, 3):
                letras = conteudo[i:(i+3)]
                self.alocacao.insert(letras)

    def open_aloc(self):
        return self.alocacao

    def read_aloc(self):
        return self.alocacao.printLL()
