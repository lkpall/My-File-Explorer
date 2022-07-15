from datetime import datetime


def date_format(_date):
    return datetime.fromtimestamp(_date).strftime('%Y-%m-%d %H:%M:%S')
