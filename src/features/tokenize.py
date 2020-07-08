from typing import List

from src.features import nlp
from src.features.utils import sentences_to_words, remove_stopwords, learn_bigrams, lemmatization


def tokenize(documents: List[str]) -> List[List[str]]:

    document_words = list(sentences_to_words(documents))
    document_words = remove_stopwords(document_words)
    document_words = learn_bigrams(document_words)
    document_words = lemmatization(nlp, document_words)

    return document_words