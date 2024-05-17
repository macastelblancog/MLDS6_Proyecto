import pandas as pd
import spacy
import re
from unidecode import unidecode
import en_core_web_sm

# Load the spaCy model
nlp = en_core_web_sm.load()

def tokenize_headlines(df, column_name):
    df['tokenized_headlines'] = df[column_name].apply(lambda x: [token for token in nlp(x)])
    return df

def filter_tokens(tokens, stopword_filter=True, length_filter=True, min_length=1, max_length=45):
    if stopword_filter:
        tokens = filter(lambda token: not token.is_stop, tokens)
    if length_filter:
        tokens = filter(lambda token: min_length <= len(token) <= max_length, tokens)
    return list(tokens)

def filter_tokenized_headlines(df, tokenized_column, stopword_filter=True, length_filter=True, min_length=1, max_length=45):
    df['filtered_tokenized_headlines'] = df[tokenized_column].apply(lambda tokens: filter_tokens(tokens, stopword_filter, length_filter, min_length, max_length))
    return df

def lemmatize_tokens(tokens):
    return [token.lemma_ for token in tokens]

def lemmatize_tokenized_headlines(df, tokenized_column):
    df['lemmatized_tokenized_headlines'] = df[tokenized_column].apply(lambda tokens: lemmatize_tokens(tokens))
    return df

def normalize_tokens(tokens):
    return [unidecode(token) for token in tokens]

def lowercase_tokens(tokens):
    return [token.lower() for token in tokens]

def clean_tokens(tokens):
    pattern = re.compile(r"[^\w\s\"']")
    return [pattern.sub('', token) for token in tokens]

def join_tokens(tokens):
    return ' '.join(tokens)

def preprocessing(df, column_name):
    df = tokenize_headlines(df, column_name)
    df = filter_tokenized_headlines(df, 'tokenized_headlines')
    df = lemmatize_tokenized_headlines(df, 'filtered_tokenized_headlines')
    df['normalized_tokenized_headlines'] = df['lemmatized_tokenized_headlines'].apply(normalize_tokens)
    df['lowercase_headlines'] = df['normalized_tokenized_headlines'].apply(lowercase_tokens)
    df['clean_r_headlines'] = df['lowercase_headlines'].apply(clean_tokens)
    df['joined_headlines'] = df['clean_r_headlines'].apply(join_tokens)
    spaces = re.compile(r"\s{2,}")
    df['joined_headlines_cleaned'] = df['joined_headlines'].apply(lambda x: re.sub(spaces, " ", x).strip())
    return df[[column_name, 'joined_headlines_cleaned']]
