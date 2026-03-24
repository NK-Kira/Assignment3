import nltk
from nltk.tree import Tree

# Variable for the sentence itself
sentence = "You should replace the blinds immediately."

# Tokenization and POS marking
text = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(text)

# Conversion of the result into a list in order to be used in the tree later
tags[0:6]

# Printing of the tokens and their tags with the sentence.
# The additional white-spaces are mostly for clarity of the output within the terminal.
print('\n')
print(tags)
print('\n')

# Creation of the tree
# Separation into two main branches
np_tree = Tree('NP', [tags[0]])
vp_tree = Tree('VP', [tags[1], tags[2], tags[3], tags[4], tags[5]])

# Combination of branches into one main tree
sentence_tree = Tree('You should replace the blinds immediately.', [np_tree, vp_tree])

# Output of the tree
sentence_tree.draw()