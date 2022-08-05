from explorer import MyFileExplorer

class AlocacaoContigua(MyFileExplorer):
    def __init__(self):
        super().__init__()

    def create_aloc(self, filename):
        with open(filename, "r") as f:
            conteudo = (f.readlines())[0]
            _max = 300
            for i in range(0, _max, 3):
                letras = conteudo[i:(i+3)]
                self.alocacao.append(letras)

    def open_aloc(self):
        return self.alocacao

    def read_aloc(self):
        alocacao_temp = self.alocacao
        conteudo = ""
        for i in range(0, 100):
            letras = alocacao_temp[i]
            conteudo += letras

        return conteudo
