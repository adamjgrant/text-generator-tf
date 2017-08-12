#import tensorflow as tf
#import numpy as np

# This is an Aesop fable passage we'll use as training data.
fable = """
long ago , the mice had a general council to consider what measures they could take to outwit their common enemy , the cat . some said this , and some said that but at last a young mouse got up and said he had a proposal to make , which he thought would meet the case . you will all agree , said he , that our chief danger consists in the sly and treacherous manner in which the enemy approaches us . now , if we could receive some signal of her approach , we could easily escape from her . i venture , therefore , to propose that a small bell be procured , and attached by a ribbon round the neck of the cat . by this means we should always know when she was about , and could easily retire while she was in the neighbourhood . this proposal met with general applause , until an old mouse got up and said that is all very well , but who is to bell the cat ? the mice looked at one another and nobody spoke . then the old mouse said it is easy to propose impossible remedies .
"""

# This will create two dictionaries, word->num and num->word
# In order for the script to work with more efficient data.
def build_dataset(passage):
  # Split the passage up into individual words

  words = passage.split(" ")
  dictionary = dict()
  
  for word in words:

    # Only consider words that have not already been added to the dictionary.
    if (dictionary.get(word) == None):
      print("Assigning {0} to dictionary whose length is {1}".format(word, len(dictionary)))
      dictionary[word] = len(dictionary)

  # Make the same hash but with the keys and values reversed for easy look up.
  reverse_dictionary = dict(zip(dictionary.values(), dictionary.keys()))

  return dictionary, reverse_dictionary

### Tensorflow shit

dictionary = build_dataset(fable)
vocab_size = len(dictionary)

# This is just the number of leading words we'll give 
# the network to make a prediction
# e.g. ["The", "cat", "ran"] as inputs possibly predicting "away"
n_input    = 3

# Not sure why this power of 2 number.
# In the tutorial, this is also referred to as "Number of units in RNN cell"
# So maybe "units" in this context means hidden neurons?
n_hidden   = 512

# These are instantiated as variables because we want to keep modifying them
# as the network runs.
# TODO: What is random_normal?
#weights    = { 'out': tf.Variable(tf.random_normal([n_hidden, vocab_size])) }
#biases     = { 'out': tf.Variable(tf.random_normal([vocab_size])) }

def RNN(x, weights, biases):
  # TODO: What is reshape, split?
  x               = tf.reshape(x, [-1, n_input])
  x               = tf.split(x, n_input, 1)
  rnn_cell        = rnn.BasicLSTMCell(n_hidden)
  outputs, states = rnn.static_rnn(rnn_cell, x, dtype=tf.float32)
  
  # Not sure why the author needed to put these in hashes with just
  # one key.
  return tf.matmul(outputs[-1], weights['out']) + biases['out']

# This happens at each step of the training process.
# We take the next three words from the training data
# and convert them into integers.
# I added the outer while loop. Not sure why it was missing
# from the example.
offset = 0
while( offset < (len(dictionary) - n_input) ):
  symbols_in_keys = []

  for i in range(offset, offset + n_input):
    word = dictionary[ str(training_data[i]) ]
    symbols_in_keys.push(word)

  offset += 1
