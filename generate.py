import tensorflow as tf
import numpy as np

# This will create two dictionaries, word->num and num->word
# In order for the script to work with more efficient data.
def build_dataset(words):
  dictionary = dict()
  
  for word in words:
    if not (bool(dictionary.get(word, False))):
      print("Assigning {0} to dictionary whose length is {1}".format(word, len(dictionary)))
      dictionary[word] = len(dictionary)
    
  reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))

  return dictionary, reverse_dictionary

dataset = build_dataset(['foo', 'bar', 'foo', 'fizz', 'bar', 'apple'])

print(dataset)
