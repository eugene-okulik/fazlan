import os
import re
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("logs", help="Directory to logs files")
parser.add_argument("--text", help="Lines search text")
args = parser.parse_args()


def get_files_directory():
    for filename in os.listdir(args.logs):
        filepath = os.path.join(args.logs, filename)
        yield filename, filepath


def read_files():
    for filename, filepath in get_files_directory():
        with open(filepath, 'r', encoding='utf-8') as data_file:
            for line_number, line in enumerate(data_file, start=1):
                yield filename, line, line_number


def search_text():
    for filename, line, line_number in read_files():
        if args.text in line:
            print(f'В файле "{filename}" на {line_number} строке найден текст "{args.text}".', end=' ')
            words = re.split(r'[-.\[\] ]+', line)
            text_index = words.index(args.text)
            start_index = max(0, text_index - 5)
            end_index = min(len(words), text_index + 6)
            words_range = words[start_index:end_index]
            print(f'Кусок строки, где был найден текст: "{" ".join(words_range)}"')


search_text()
