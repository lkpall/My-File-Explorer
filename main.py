import os
import shutil
from typing import Dict

from utils import date_format


class MyFileExplorer:
    def __init__(self):
        self.alocacao = []

    def get_file_attr(self, filename: str) -> Dict:
        id = os.stat(filename).st_uid,
        name = filename,
        tamanho = os.path.getsize(filename),
        data_criacao = date_format(os.path.getctime(filename)),
        data_mod = date_format(os.path.getmtime(filename))

        return f"{id[0]} {name[0]} {tamanho[0]} {data_criacao[0]} {data_mod}"

    def list_items_path(self):
        items = os.listdir(self.get_path_current_dir())

        for item in items:
            print(self.get_file_attr(item))

    def join_path_url(self, item_name: str) -> str:
        return os.path.join(self.get_path_current_dir(), item_name)

    def get_path_current_dir(self) -> str:
        return os.getcwd()

    def current_dir(self) -> None:
        print(self.get_path_current_dir())

    def create_folder(self, dirname: str) -> None:
        os.mkdir(self.join_path_url(dirname))

    def change_dir(self, dirname: str) -> None:
        try:
            os.chdir(self.join_path_url(dirname))
        except IsADirectoryError:
            print("Diretorio inexistente!")

    def rename_dir(self, dirname, new_dirname):
        source_name = self.join_path_url(dirname)
        new_name = self.join_path_url(new_dirname)
        try:
            os.rename(source_name, new_name)
        except IsADirectoryError:
            print("Diretorio inexistente!")

    def delete_folder(self, dirname: str) -> None:
        dir_path = self.join_path_url(dirname)

        if os.path.exists(dir_path):
            # Verifica se a pasta está vazia
            if len(os.listdir(dir_path)) == 0:
                os.rmdir(dir_path)
            else:
                print("A pasta nao esta vazia!")
        else:
            print("O diretorio nao existe!")

    def create_file(self, filename: str) -> None:
        try:
            with open(filename, 'w'):
                pass
        except IsADirectoryError:
            print("Jah existe um item com esse nome. Tente outro nome!")

    def delete_file(self, filename: str):
        try:
            os.remove(self.join_path_url(filename))
        except IsADirectoryError:
            print("Arquivo desconhecido!")

    def move_file(self, filename: str, target: str) -> None:
        """
        Params:
            filename: nome do arquivo no diretorio atual
            target: destino do arquivo

        Obs: O destino do arquivo tem que ser a partir do diretorio atual
        """

        source = self.join_path_url(filename)

        if target.endswith(("/", r"'\'")):
            target = target+filename

        destination = self.join_path_url(target)

        shutil.move(source, destination)

    def copy_file(self, filename: str, new_filename: str) -> None:
        if filename == new_filename:
            print("Os nomes estao iguais, tente outro nome!")
            return

        shutil.copy(filename, new_filename)

    def write_text(self, filename: str) -> None:
        with open(self.join_path_url(filename), 'a') as f:
            text = input("Digite aqui $> ")
            f.write(text)
            
    def read_text(self, filename: str) -> None:
        if os.path.exists(self.join_path_url(filename)):
            with open(self.join_path_url(filename), 'r') as f:
                print(f.readlines())
        else:
            print("Arquivo inexistente!")

    def criar_contigua(self, filename, loc):
        if loc == "contigua":
            with open(filename, "r") as f:
                conteudo = (f.readlines())[0]
                j = 0
                for i in range(0, 100):
                    letras = conteudo[i:(j+3)]
                    self.alocacao.append(letras)
                    j += i+3
            
            return self.alocacao

    def abrir(self, filename, alocacao="contigua"):
        if alocacao == "contigua":
            return self.alocacao

    def ler(self, filename, alocacao):
        alocacao_temp = self.criar_contigua("renata.txt")
        conteudo = ""
        if alocacao == "contigua":
            for i in range(0, 100):
                letras = alocacao_temp[i]
                conteudo += letras
            
            return conteudo


mfe = MyFileExplorer()

dict_commands = {
    "createfolder": mfe.create_folder,
    "deletefolder": mfe.delete_folder,
    "cd": mfe.change_dir,
    "rename": mfe.rename_dir,
    "createfile": mfe.create_file,
    "deletefile": mfe.delete_file,
    "movefile": mfe.move_file,
    "copyfile": mfe.copy_file,
    "ls": mfe.list_items_path,
    "nano": mfe.write_text,
    "cat": mfe.read_text,
    "pwd": mfe.current_dir
}

while True:
    current_dir = mfe.get_path_current_dir()
    command = input(f"{current_dir} #> ")
    args = command.split()
    try:
        if len(args) > 1:
            dict_commands[args[0]](*args[1:])
        else:
            dict_commands[args[0]]()
    except KeyError:
        print('Comando invalido!')

