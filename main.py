from contigua import AlocacaoContigua
from indexada import AlocacaoIndexada
from encadeada import AlocacaoEncadeada

aloc = input("Escolha uma das opcoes de alocacao:\n 1 - Contigua\n 2 - Encadeada\n 3 - Indexada\n\n =>")

aloc_options = {
    '1': AlocacaoContigua,
    '2': AlocacaoEncadeada,
    '3': AlocacaoIndexada,
}

mfe = aloc_options[aloc]()

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
    "pwd": mfe.current_dir,
    "createaloc": mfe.create_aloc,
    "openaloc": mfe.open_aloc,
    "readaloc": mfe.read_aloc
}

while True:
    current_dir = mfe.get_path_current_dir()
    command = input(f"{current_dir} #> ")
    args = command.split()
    try:
        if len(args) > 1:
            r = dict_commands[args[0]](*args[1:])
        else:
            r = dict_commands[args[0]]()

        if r:
            print(r)
    except KeyError:
        print('Comando invalido!')
