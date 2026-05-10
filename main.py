import argparse
import csv
from tabulate import tabulate

CTR = 15.0
RETENTION_RATE = 40
HEADERS_TEMPLATE = [
    'title', 'ctr', 'retention_rate', 'views', 'likes', 'avg_watch_time'
]
report_data_unsort = []
ctr_order = []
report_data_sort = []


def create_parser():
    """
    Инициализация parser.
    """
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


def validate_files_names(args):
    """
    Проверка указанных в параметрах файлов.
    :param args:
    :return:
    """
    if args.files is None:
        raise ValueError(
            'Не указаны файлы после параметра --files.'
        )
    if args.report is None:
        raise ValueError(
            'Не указано имя выходного файла после параметра --report.'
        )


def validate_files_format(filename):
    """
    Проверка формата входных файлов.
    """
    if filename[-4:] != '.csv':
        raise ValueError(f'Файл {filename} должен быть в формате csv')


def validate_headers(headers):
    """
    Проверка формата header/шапки/названий столбцов входных файлов.
    :param headers:
    :return:
    """
    if headers != HEADERS_TEMPLATE:
        raise ValueError(
            f'''Шапка/header не соответствует ожидаемому.
            Получено: {headers}
            Ожидалось {HEADERS_TEMPLATE}
            '''
        )


def extract_necessary_data(filenames):
    """
    Выборка нужных строк.
    :param filenames:
    :return:
    """
    for filename in filenames:
        validate_files_format(filename)
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            headers = next(reader)
            validate_headers(headers)
            for row in reader:
                if float(row[1]) > CTR and int(row[2]) < RETENTION_RATE:
                    report_data_unsort.append([row[0], float(row[1]), row[2]])
                    ctr_order.append(float(row[1]))
    return headers, report_data_unsort, ctr_order


def sort_data(ctr_order, report_data_unsort):
    """
    Сортировка в порядке убывания полученных строк по ctr.
    :param ctr_order:
    :param report_data_unsort:
    :return:
    """
    for index in range(len(ctr_order)):
        min_ctr_number = max(ctr_order)
        index_min_ctr_number = ctr_order.index(min_ctr_number)
        report_data_sort.append(report_data_unsort.pop(index_min_ctr_number))
        del ctr_order[index_min_ctr_number]
    return report_data_sort


def write_to_file(file_write, report_data_sort):
    """
    Запись полученных данных в выходной файл.
    :param file_write:
    :param report_data_sort:
    :return:
    """
    with open(file_write, 'w', encoding='utf-8') as write_file:
        writer = csv.writer(write_file)
        for row in report_data_sort:
            writer.writerow(row)


def module_main():
    """
    Главная функция, собирающая все шаги.
    """
    args = create_parser().parse_args()
    validate_files_names(args)
    headers, report_data_unsort, ctr_order = extract_necessary_data(args.files)
    report_data_sort = sort_data(ctr_order, report_data_unsort)
    write_to_file(args.report, report_data_sort)
    return tabulate(report_data_sort, headers, tablefmt='grid')


if __name__ == "__main__":
    print(module_main())
