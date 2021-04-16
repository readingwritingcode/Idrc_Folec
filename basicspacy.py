# pip install -U spacy .... donde
# python -m spacy download sp_core_web_lg

import spacy

# load trained model
nlp = spacy.load("sp_core_web_lg")

# proccess documents 
text = ("some text here")

doc = nlp(doc)

# Analyze syntax
noun_phrases = [chunk.text for chunk in doc.noun_chunks]
verbs = [token.lemma_ for token in doc if token.pos_ == "VERB"]  # NOTE: tokens have certain attributes

# name entitiesm phrases and concepts

for entity in doc.ents:
    print(entity.text, entity.label_)

# https://spacy.io/usage/linguistic-features

# linguistic features
# part of speech taggin

import spacy

nlp = spacy.load('sp_core_web_lg')

doc = nlp("some text here!")

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.tag_, token.tag_, token.dep_,
    token.shape_, token.is_alpha, token.is_stop)


'''
text: the original word text.
lemma: the base form of the word.
POS: the simple UPOS part-of-speech tag. -> https://universaldependencies.org/docs/u/pos/
    Alphabetical listing

    ADJ: adjective
    ADP: adposition
    ADV: adverb
    AUX: auxiliary verb
    CONJ: coordinating conjunction
    DET: determiner
    INTJ: interjection
    NOUN: noun
    NUM: numeral
    PART: particle
    PRON: pronoun
    PROPN: proper noun
    PUNCT: punctuation
    SCONJ: subordinating conjunction
    SYM: symbol
    VERB: verb
    X: other




Dep: Syntactic dependency, i.e. the relation between tokens.
Shape: the word shape
is alpha: is the token alpha character
is stop: is the token part of a stop list. the most common words of the language?


'''

# lexical attributes

from spacy.lang.en import English

nlp = English()

# Process the text
doc = nlp(
    "In 1990, more than 60% of people in East Asia were in extreme poverty. "
    "Now less than 4% are."
)

# Iterate over the tokens in the doc
for token in doc:
    # Check if the token resembles a number
    if token.like_num:
        # Get the next token in the document
        next_token = doc[token.i+1]
        # Check if the next token's text equals "%"
        if next_token.text == "%":
            print("Percentage found:", token.text)

# https://spacy.io/usage/rule-based-matching

# sintactic dependencies: how the words are related

from spacy.lang.en import English
nlp = English()
doc = English("She ate the pizza")
for token in doc:
    print(token.text, token.pos_, token.dep_, token.head.text)

# pos -> tags
# sd -> tags

# prdicting Named Entities

doc = nlp("Apple is looking a buying U.K startup for $1 billion")

for ent in doc.ents:
    print(ent.text, ent.label_)

# get kick definitions of the most common tags and labels.
spacy.explain("GPE")

spacy.explain("NNP")