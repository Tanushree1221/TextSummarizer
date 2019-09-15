# importing the necessary packages
import spacy 
nlp = spacy.load('en')
# Finding the Top N Sentences
from heapq import nlargest
# Packages that are reuired for Normalizing Text
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation




def textSummarizer(raw_docx):
    
    raw_text = raw_docx
    docx = nlp(raw_text)
    stopwords = list(STOP_WORDS)
    # Build Word Frequency # word.text is tokenization in spacy
    word_frequencies = {}  
    for word in docx:  
        if word.text not in stopwords:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1


    maximumFrequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximumFrequncy)
    # Sentence Tokens
    sentence_list = [ sentence for sentence in docx.sents ]

    #Calculate Sentence Scores
    sentence_scores = {}  
    for sente in sentence_list:  
        for word in sente:
            if word.text.lower() in word_frequencies.keys():
                if len(sente.text.split(' ')) < 30:
                    if sente not in sentence_scores.keys():
                        sentence_scores[sente] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sente] += word_frequencies[word.text.lower()]

    # Find N Largest and Join Sentences
    summarized_sentences = nlargest(7, sentence_scores, key=sentence_scores.get)
    final_sentences = [ w.text for w in summarized_sentences ]
    summary = ' '.join(final_sentences)
    print("Original Document\n")
    print(raw_docx)
    print("Total Length:",len(raw_docx))
    print('\n\nSummarized Document\n')
    print(summary)
    print("Total Length:",len(summary))
    




# Jesse JCharis
# Jesus Saves@JCharisTech