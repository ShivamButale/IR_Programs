'''
Assignment 6: 
Using wordnet nltk library:
1) Print all noun words present in wordnet.
2) Print the different senses or meanings of the given word.
3) Print all synonyms for the given word. Also count them.
4) Print the antonyms of the given word.
5) Print the number of senses of the given word in all parts-of-speech category like noun, verb, adverb and adjective.
6) Find the semantic similarity between the given words.
7) For the given word print its hypernym and co-hyponyms.
8) For the given word print its hyponyms.
9) Find all the words related to sports domain from wordnet.
'''
from nltk.corpus import wordnet as wn

def return_senses(word, pos):
	if pos == 'n':
		pos1 = "Noun"
	if pos == 'v':
		pos1 = "Verb"
	if pos == 'a':
		pos1 = "Adjective"
	if pos == 'r':
		pos1 = "Adverb"
	
	senses = list()
	for synset in wn.synsets(word):
		words = wn.synsets(synset.lemmas()[0].name(), pos = pos)
		if len(words) != 0:
			senses.extend(word.lemmas()[0].name() for word in words)
	print("Number of senses with POS Category : '" + pos1 + "' = ",len(senses))
	if len(senses):
		print(senses)

	
def semantic_similarity(word1, word2):
	w1 = wn.synset(wn.synsets(word1)[0].name())
	print(w1)
	w2 = wn.synset(wn.synsets(word2)[0].name())
	print(w2)
	print(w1.wup_similarity(w2))
	print("\n")
	
def main():
	'''
	#1)Print all Noun words present in Wordnet              -----------------------------------------------
	
	print("Following are all the nouns in wordnet: ")
	all_nouns = []
	for i in wn.all_synsets('n'):
		all_nouns.append(i.name().split(".")[0])
	for i in all_nouns:
		print(i)
	print("\n")
	
	'''
	#2)Print the different senses or meanings of the given word              -----------------------------------------
	
	print("Enter a word : ")
	word = input()
	
	sent = []
	for i, syn in enumerate(wn.synsets(word)):
		synsets = wn.synsets(syn.lemmas()[0].name())
		for j in range(0, len(synsets)):
			t = synsets[j].definition()
			if t not in sent:
				sent.append(t)		
	for i in sent:
		print(i)
	
	
	#3)Print all synonyms for the given word. Also count them.	 -------------------------------------------------------------------------
	
	print("\n")
	synonyms = set()
	for i in wn.synsets(word):
		for l in i.lemmas():
			synonyms.add(l.name())
			if l.antonyms():
				antonyms.add(l.antonyms()[0].name())
	
	print("The Synonyms of the given word are : \n")
	for synonym in synonyms:
		print(synonym)
	print("Number of synonyms =  " ,len(synonyms))
	print("\n")

	#4)Print the antonyms of the given word  -----------------------------------------------------------------------------------------------------
	
	antonyms = set()
	for i in wn.synsets(word):
		for l in i.lemmas():
			if l.antonyms():
				antonyms.add(l.antonyms()[0].name())	
	print("The Antonyms of the given word are : ")	
	for antonym in antonyms:
		print(antonym)
	print("Number of antonyms = ", len(antonyms))
	print("\n")
	
	#5)Print the number of senses of the given word in all parts-of-speech category like noun, verb, adjective and adverb   -------------------------
	
	pos = ['n', 'v', 'a', 'r']
	for i in pos:
		return_senses(word, i)
	
	#6)Find the semantic similarity between the given words.                   -----------------------------------
	
	print("\n")
	n = int(input("Enter the number of words to be input : "))
	for i in range(n):
		print("Please enter a word : ")
		word2 = input()
		semantic_similarity(word, word2)	
	
	#7)For the given word print its hypernym and co-hyponyms.              -----------------------
	
	print("\n")
	hypernyms = set()
	co_hyponyms = set()

	for i in wn.synsets(word):
		for hypernym in i.hypernyms():
			hypernyms.add(hypernym.lemmas()[0].name())
	print("Following are the hypernyms : \n")
	for hyper in hypernyms:
		print(hyper)
	print("\n")
	
	for hypernym in hypernyms:
		for i in wn.synsets(hypernym):
			for hyponym in i.hyponyms():
				co_hyponyms.add(hyponym.lemmas()[0].name())
	print("Following are the Co-hyponyms : \n")
	for co in co_hyponyms:
		print(co)
	print("\n")
	
	
	#8) For the given word print its hyponyms                ----------------------------
	hyponyms = set()
	for i in wn.synsets(word):
		for hyponym in i.hyponyms():
			hyponyms.add(hyponym.lemmas()[0].name())
	print("Following are the hyponyms : \n")
	for hypo in hyponyms:
		print(hypo)
	print("\n")
	
	
	#9)Find all the words related to sports domain from wordnet               ----------------
	result = set()
	sports = wn.synsets('sports', pos = 'n')
	hypo = lambda s: s.hyponyms()
	for i in sports:
		for synset in list(i.closure(hypo)):
			result.add(synset.lemmas()[0].name())
	print("Following are the Words related to sports in Wordnet : ")
	for i in result:
		print(i)
	print("\n")
	
main()
