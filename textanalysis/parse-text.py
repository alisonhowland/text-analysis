# ------------------------------------------------------------------------
# Script for text parsing and analysis
# Reads a text file and returns analysis in the console in table format:
#    - number of individual words
#    - number of words with >5 characters
#    - mumber of words with <5 characters
#    - number of words with an even amount of characters
#    - number of words with an odd amount of characters# 
# ------------------------------------------------------------------------
# Created 3-3-2018
# Author: Alison Howland
# alisonhowland@gmail.com
# ------------------------------------------------------------------------

import nltk
from string import punctuation
import sys
from terminaltables import AsciiTable


# ------------------------------------------------------------------------
#     FUNCTIONS
# ------------------------------------------------------------------------
# Reads a file and stores as a single string.
# Parameter:  file -- the filepath to be read
# Returns  :  text -- the contents of the file, read and stored
#                     in a single string.
# Exceptions: throws IOError or OSError (depending on reason for failure
#             if file is unable to be opened or read.
def read_file(file):
    text = str()
    try:
        temp = open(file, 'r')
        text = temp.read().lower()
    except (IOError, OSError):
        print("  Could not open " + file)
        quit()
    else:
        print("File: '" + str(file) + "' ")
    temp.close()
    return text


# Tokenizes a given text by word; stores all tokens in a single set
#     containing all distinct words present in the set.
# Parameter:  text -- a single string containing all text to be tokenized.
# Returns  :  set  -- a set containing all distinct words present in the text.
#                     All tokens consisting of a single punctuation mark are
#                     removed. (Ex: '?', '[', '.', etc.)
#                     Contractions are split into two words:
#                        Ex: "don't" -> "do", "n't"
def create_word_set(text):
    word_set = set(nltk.word_tokenize(text))
    return word_set


# Parameters: filename --  must exist
#             data     --  set or list of text analysis data
def save_output(data, filename):
    try:
        f = open(resp, 'a')
    except IOError:
        print("File not found")
    except:
        print("Unexpected error")
    f.write("%s\n" % filename)
    for item in data:
        f.write("%s\n" % item)
        f.close


# -----------------------------------------------------------------------------
#    PROGRAM SCRIPT
# -----------------------------------------------------------------------------
# Command line argument --  file to be read
filename = sys.argv[-1]
text = str()  # Single string to hold all text file input

# Read file
text = read_file(filename)

# Variables to hold word analysis counts
words_over_5 = 0  # Words with >5 characters
words_under_5 = 0  # Words with <5 characters
odd_words = 0  # Words with an odd number of characters
even_words = 0  # Words with an even number of characters

word_set = sorted(set(create_word_set(text)))  # All distinct words in the text

# Remove set items that are only punctuation
for item in word_set[:]:
    if item.strip() in punctuation:
        word_set.remove(item)

# Loop through set and get character counts
for item in word_set:
    if len(item) < 5:
        words_under_5 += 1  # Word has <5 characters
    elif len(item) > 5:
        words_over_5 += 1   # Word has >5 characters
    if len(item) % 2 == 0:
        even_words += 1     # Word has even number of characters
    elif len(item) % 2 == 1:
        odd_words += 1      # Word has odd number of characters

distinct_word_count = len(word_set)

# Display results
data = []
data.append(['Total word count (distinct)', distinct_word_count])
data.append(['Words with <5 characters', words_under_5])
data.append(['Words with >5 characters', words_over_5])
data.append(['Words with odd number of chars', odd_words])
data.append(['Words with even number of chars', even_words])

# Formatted table for output
output = AsciiTable(data)
output.title = "Text analysis"

print()
print(output.table)

resp = input("Press q to quit, or enter filename to save output: ")

if resp.lower().strip() == 'q':
    quit()
else:
    save_output(data, resp)

print("Output saved to '" + resp + "' ")
quit()
