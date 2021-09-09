from docx import Document
import numpy as np
import csv
import re
import argparse


class Parser():
    def __init__(self, filename):
        self.filename = filename
        self.document = document = Document(filename)
        self.question_numbers = []
        self.question_text = []
        self.question_array = []

    def parse_questions(self):
        for table in self.document.tables:
            if len(table.rows) != 1:
                continue
            cell_text = table.cell(0, 0).text
            match = bool(re.match(r'\d[\.\d\.]*\d\s', cell_text))
            if match:
                question_number = cell_text[:cell_text.find(' ')].strip()
                question_text = cell_text.replace(question_number, '').strip()
                self.question_numbers.append(question_number)
                self.question_text.append(question_text)
                self.question_array.append([question_number, question_text])

    def save_to_csv(self, filename):
        with open(filename, 'w') as f:
            csv.writer(f).writerows(self.question_array)

    def get_question_text(self):
        return self.question_text

    def get_question_numbers(self):
        return self.question_numbers


def main():
    parser = argparse.ArgumentParser(description="Parse afme files")
    parser.add_argument('file', help='A required integer positional argument')
    args = parser.parse_args()
    print(args.file)
    parser = Parser(args.file)
    parser.save_to_csv('data/test.csv')


if __name__ == "__main__":
    main()
