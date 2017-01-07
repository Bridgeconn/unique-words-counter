import os, sys, codecs
from string import punctuation
from collections import Counter

if len(sys.argv) < 2:
    print('''No input file given.

Usage: python3 count.py /path/to/file
''')
    exit()

# Accept command line argument
filePath = sys.argv[1]

# Check if the path given exists
if not os.path.exists(filePath):
    print('Error. Given path is not a valid file.')
    exit()

# The only function in this program
def count():
    entries = []

    # Open the file given as argumentas in utf-8
    with codecs.open(filePath, 'r', 'utf-8') as f:

        # Read all contents of the file
        contents = f.read()

        # Characters to clean-up around each word
        puncts = punctuation
        puncts += "“”।’‘"

        # filter out words and strip punctuations around each word
        cleaned_contents = ' '.join(filter(None, (word.strip(puncts) for word in contents.split())))

        # Split the cleaned_contents in to words and count occurances. This reponds with a dict.
        kv = Counter(cleaned_contents.split())

        # Convert the dict in to an array of tuples like [(word1, 4), (word2, 5)]
        for k in kv:
            entries.append((k, kv[k]))
    # Sort the array
    entries = sorted(entries, key=lambda x: x[1])

    # Finally write out the words and their frequencies
    with codecs.open(filePath + '.tab', 'w', 'utf-8') as w:
        for e in entries:
            w.write(e[0])
            w.write('\t')
            w.write(str(e[1]))
            w.write('\n')

# Finally call the count() function
count()
