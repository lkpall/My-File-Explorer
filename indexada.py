from explorer import MyFileExplorer


class AlocacaoIndexada(MyFileExplorer):
    def __init__(self):
        super().__init__()
        self.alocacao = {}

    def create_aloc(self, filename):
        with open(filename, "r") as f:
            conteudo = (f.readlines())[0]
            _max = 200
            count = 0

            for i in range(0, _max, 2):
                self.alocacao[count] = [conteudo[i], conteudo[i+1]]
                count += 1

    def open_aloc(self):
        return self.alocacao

    def read_aloc(self):
        alocacao_temp = self.alocacao
        conteudo = ""

        for i in range(0, 100):
            letras = alocacao_temp[i][0] + alocacao_temp[i][1]
            conteudo += letras

        return conteudo
