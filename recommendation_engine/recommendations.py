import os
import re
from docx import Document
import csv
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import sys
import helpers


class Recommendations():

    def __init__(self, model_type='msmarco-distilbert-base-v4'):
        self.model_type = model_type
        self.model = SentenceTransformer('msmarco-distilbert-base-v4')

    def build_model(self, sentences=[]):
        self.sentences = sentences
        self.sentence_array = np.asarray(sentences)
        self.sentence_embeddings = self.model.encode(sentences)

    def print_matches(self, text, matches=5):
        text_embedding = self.model.encode([text])
        scores = cosine_similarity(
            [text_embedding[0]],
            self.sentence_embeddings
        )
        scores = scores[0]
        indices = np.argpartition(scores, -matches)[-matches:]
        indices = indices[np.argsort(-1 * scores[indices])]
        for index in indices:
            print(str((scores[index] * 100).round(1)) +
                  "%: " + str(self.sentence_array[index]))
        print("\n\n")


def main():
    parser = helpers.Parser('data/afme.docx')
    parser.parse_questions()
    recommend = Recommendations()
    recommend.build_model(parser.get_question_text())

    while True:
        txt = input("Enter question text: ")
        recommend.print_matches(txt)


if __name__ == "__main__":
    main()
