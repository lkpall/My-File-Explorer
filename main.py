import os
import shutil
from typing import Dict

from utils import date_format


class MyFileExplorer:
    def __init__(self):
        pass

    def get_file_attr(self, filename: str) -> Dict:
        attrs = {
            'name': filename,
            'tamanho': os.path.getsize(filename),
            'data_mod': date_format(os.path.getmtime(filename)),
            'data_criacao': date_format(os.path.getctime(filename)),
            'id': os.stat(filename).st_uid
        }

        return attrs

    def list_items_path(self):
        items = os.listdir(self.get_path_current_dir())

        for item in items:
            print(self.get_file_attr(item))

    def join_path_url(self, item_name: str) -> str:
        return os.path.join(self.get_path_current_dir(), item_name)

    def get_path_current_dir(self) -> str:
        return os.getcwd()

    def create_folder(self, dir_name: str) -> None:
        os.mkdir(self.join_path_url(dir_name))

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


mfe = MyFileExplorer()

dict_commands = {
    "createfolder": mfe.create_folder,
    "createfile": mfe.create_file,
    "deletefile": mfe.delete_file,
    "movefile": mfe.move_file,
    "copyfile": mfe.copy_file,
    "ls": mfe.list_items_path
}

while True:
    command = input("#> ")
    args = command.split()
    try:
        if len(args) > 1:
            dict_commands[args[0]](args[1])
        else:
            dict_commands[args[0]]()
    except KeyError:
        print('Comando invalido!')

