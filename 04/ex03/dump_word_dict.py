"""
python dump_word_dict.py
python -m pickle word_count.pickle
"""
import json
import pickle
import pprint

filename = "words.txt"
dmp_filename = "word_count.pickle"
d = {}
with open(filename) as f:
    for line in f:
        line = line.strip()
        line = line.lower()
        words = line.split()
        for word in words:
            word = word.strip()
            word_length = len(word)
            if word_length in d:
                d[word_length] += 1
            else:
                d[word_length] = 1

with open(dmp_filename, 'wb') as binary_file:
    pickle.dump(d, binary_file)
    # pickle.dump(d, binary_file, protocol= pickle.DEFAULT_PROTOCOL)
    # pickle.dump(d, binary_file, pickle.HIGHEST_PROTOCOL, fix_imports=True)

# dmp = pickle.dumps(d)
# print(dmp)
# with open(dmp_filename, 'wb') as binary_file:
#     binary_file.write(dmp)
