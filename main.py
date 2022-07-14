import os

from datetime import datetime


def get_file_attr(filename):
    attrs = {
        'tamanho': os.path.getsize(filename),
        'data_mod': date_format(os.path.getmtime(filename)),
        'data_criacao': date_format(os.path.getctime(filename)),
        'id': os.stat(filename).st_uid
    }
 
    return attrs

def date_format(_date):
    return datetime.fromtimestamp(_date).strftime('%Y-%m-%d %H:%M:%S')

filename = 'texto.txt'
print(get_file_attr(filename))

