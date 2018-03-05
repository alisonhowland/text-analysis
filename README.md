# text-analysis
Python script to read a text file, analyze it, then output (and save, if desired) the following analysis results to the terminal: 

  - number of distinct words present in the text
  - number of words with fewer than five characters
  - number of words with more than five characters
  - number of words with an even number of characters
  - number of words with an odd number of characters

# Dependencies

### [nltk](https://www.nltk.org/install.html):

    $ pip3 install nltk
    
Check installation by running `python3` if installed with `pip3` (or `python` if installed with `pip`) then `import nltk`.

### [terminaltables](https://github.com/Robpol86/terminaltables):

    $ pip3 install terminaltables

text-analysis was created and tested using Python 3, but should work with Python 2.x as well. Example and instructions on this page use `python3` and `pip3`; substitute with `python` and `pip` where needed. 

# Usage
## [parse-text.py](https://github.com/alisonhowland/text-analysis/blob/master/textanalysis/parse-text.py)
This simple script runs straight from the command line and outputs results in an ASCII table format. 

To use, first install nltk and terminaltable dependencies using the above commands. See the respective links for more information, if needed. 

Download the `parse-text.py` file linked above. If saved output is desired, have an file ready for writing. Output will be appended to any existing data in a file. 

The target text should be in a separate file. UTF-8 is supported; see nltk documentation for further details about file types and tokenizing processes. The text file is passed as a command-line argument with `parse-text.py`. (see below) 

## Example 

Say we have text file `sample.txt`:

    $ cat sample.txt
    If you're happy and you know it, clap your hands!

To analyze the text:
    
    $ python3 parse-text.py sample.txt
    File: 'sample.txt'

    +Text analysis--------------------+----+
    | Total word count (distinct)     | 10 |
    +---------------------------------+----+
    | Words with <5 characters        | 8  |
    | Words with >5 characters        | 0  |
    | Words with odd number of chars  | 5  |
    | Words with even number of chars | 5  |
    +---------------------------------+----+
    Press q to quit, or enter filename to save output: output.txt
    Output saved to 'output.txt'
    
Notice how the total word count is 10, not 11. The tokenization of "you're" creates "you" and "'re", resulting in two instances of the word "you". Only distinct words are counted.

If saved output is desired, the file need not be empty; text-analysis will append data to the end. The filename will print followed by the results: 
    
    $ cat output.txt
    output.txt
    ['Total word count (distinct)', 10]
    ['Words with <5 characters', 8]
    ['Words with >5 characters', 0]
    ['Words with odd number of chars', 5]
    ['Words with even number of chars', 5]


# Further details

Duplicate words are not considered in any of the counts returned.

Contractions are split into two words, and punctuation within a word counts toward the character count. For example: ("don't") results in the tokens ("do" , "n't"), with respective character counts of 2 and 3.

Numbers are considered words and are counted. For example: "153rd" is considered a five-character "word"

# Lastly

Package and additional dependency files (setup.py, etc.) are not yet complete, so `pip` installation is not currently supported. Contact the author with any further questions.  
