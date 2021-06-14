from math import sqrt
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

def removeStopwords (phrase):
    noStopwords = []
    for word in phrase:
        if word not in stopwords:
            noStopwords.append(word)

    return noStopwords

def stemmingPhrase (phrase):
    stemmed = []
    for word in phrase:
        stem = stemmer.stem(word)
        stemmed.append(stem)

    return stemmed

language = input("\n > Select a language: ").lower()

stopwords = stopwords.words(language)
stemmer = SnowballStemmer(language)

userStringFirst = input("\n > Enter first phrase: ").lower().split(" ")
userStringSecond = input("\n > Enter second phrase: ").lower().split(" ")

# Remove STOPWORDS
noStopwordsFirst = removeStopwords(userStringFirst)
noStopwordsSecond = removeStopwords(userStringSecond)

# STEMMING
stemmedFirst = stemmingPhrase(noStopwordsFirst)
stemmedSecond = stemmingPhrase(noStopwordsSecond)

# SORTING
stemmedFirst.sort()
stemmedSecond.sort()

# FREQUENCY CALCULATION
numerator = 0
factorFirst = 0
factorSecond = 0

alredyCountedFirst = []
for wordRadical in stemmedFirst:
    if wordRadical not in alredyCountedFirst:
        frequencyFirst = stemmedFirst.count(wordRadical)
        frequencySecond = stemmedSecond.count(wordRadical)

        numerator += frequencyFirst * frequencySecond
        factorFirst += frequencyFirst ** 2

        alredyCountedFirst.append(wordRadical)

alredyCountedSecond = []
for wordRadical in stemmedSecond:
    if wordRadical not in alredyCountedSecond:
        frequencySecond = stemmedSecond.count(wordRadical)

        factorSecond += frequencySecond ** 2

        alredyCountedSecond.append(wordRadical)

# SIMILARITY CALCULATION
similarity = round(((numerator / sqrt(factorFirst * factorSecond)) * 100), 2)

print(f"\n > The phrases are {similarity}% similar")