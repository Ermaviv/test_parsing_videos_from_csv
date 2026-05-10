import argparse
import pytest

NAME_FIX_FILE_1 = 'fix_data_1.csv'
NAME_FIX_FILE_2 = 'fix_data_2.csv'
NAME_FIX_REPORT = 'fix_report'

fix_file = [
    ['title', 'ctr', 'retention_rate', 'views', 'likes', 'avg_watch_time'],
    ['Я бросил IT и стал фермером', 18.2, 35, 45200, 1240, 4.2],
    ['Как я спал по 4 часа и ничего не понял', 22.5, 28, 128700, 3150, 3.1],
    ['Почему сеньоры не носят галстуки', 9.5, 82, 31500, 890, 8.9]
]


@pytest.fixture()
def fix_create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--files',
        help='Перечень файлов для чтения',
        nargs='+',
        required=True
    )
    parser.add_argument(
        '--report',
        help='Отчетный файл',
        required=True
    )
    return parser
