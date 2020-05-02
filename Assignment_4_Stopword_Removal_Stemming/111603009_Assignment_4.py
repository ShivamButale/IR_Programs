from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer 

stop_words = set(stopwords.words('english')) 
file1 = open("original_text.txt")
f1 = open('removed_stopwords_text.txt','w') 
f2 = open('stemmed_text.txt','w')

line = file1.read()
words = line.split() 
for i in words: 
	if not i in stop_words: 
		f1.write(" "+i) 

ps = PorterStemmer() 
#line = "Programers program with programing languages"
words = word_tokenize(line) 
for w in words: 
	f2.write(ps.stem(w)) 
	f2.write(" ")
