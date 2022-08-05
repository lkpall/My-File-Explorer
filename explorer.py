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
