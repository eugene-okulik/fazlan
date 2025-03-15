import os
import csv
import dotenv
import collections
import mysql.connector as mysql

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
file_path = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)

cursor = db.cursor()


def read_file():
    with open(file_path, 'r', encoding='utf-8') as data_file:
        for row in csv.DictReader(data_file):
            yield row


def update_data():
    data = collections.defaultdict(list)
    for line in read_file():
        for key, value in line.items():
            if value not in data[key]:
                data[key].append(value)
    return data


def update_attribute():
    data = update_data()
    for attribute, values in data.items():
        if 'subject' in attribute:
            attribute = attribute.split('_')
            table, attribute = 'subjets', attribute[1]
        elif 'title' in attribute:
            attribute = attribute.split('_')
            table, attribute = attribute[0] + 's', attribute[1]
        elif 'value' in attribute:
            attribute = attribute.split('_')
            table, attribute = attribute[0] + 's', attribute[1]
        else:
            table = 'students'
        yield attribute, table, values


def print_out_data_in_db():
    for attribute, table, values in update_attribute():
        for value in values:
            select_q = "SELECT count(*) FROM `{}` WHERE `{}` = %s".format(table, attribute)
            cursor.execute(select_q, (value,))
            count = cursor.fetchone()[0]
            if count == 0:
                print(f'В таблице "{table}" в поле "{attribute}" отсутствует значение "{value}"')


print_out_data_in_db()
