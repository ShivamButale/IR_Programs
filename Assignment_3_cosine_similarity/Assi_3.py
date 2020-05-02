#															IR ASSIGNMENT 3 
#																			Author - Shivam Milind Butale
#																			MIS - 111603009
#Python Program for Assignment 3 - Read three documents, represent them in Vector Space Model, find cosine similarity between the documents(use tf-idf)
import math
def remove_newline(thisline):
	z=thisline[-1]
	ff=[]
	for i in z:
		if i != '\n':
			ff.append(i)
	str = "".join(ff)	
	thisline[-1] = str

def remove_duplicates(all_words):
	z = []
	for i in all_words:
		if i not in z:
			z.append(i)
	return z

def construct_dataset(thisline1, thisline2, thisline3):
	for i in thisline1:
		all_words.append(i)
	for i in thisline2:
		all_words.append(i)
	for i in thisline3:
		all_words.append(i)
	
def create_vector_space_model1(all_words, thisline1, thisline2, thisline3):
	doc1 = []
	N = 3 #no of docs
	'''
	idf = log(N/df)
	W = (1 + log tf) * idf
	'''
	for i in all_words:
		tf=0
		df=0
		for j in range(0, len(thisline1)):
			if thisline1[j] == i:
				tf=tf+1
		if i in thisline1:
			df=df+1	
		if i in thisline2:
			df=df+1
		if i in thisline3:
			df=df+1
		if(tf > 0):	
			term1 = 1 + math.log(tf,10)
		else:
			term1 = 0
		idf = math.log((N/df), 10)
		term2 = idf
		tf_idf = term1 * term2
		doc1.append(tf_idf)
	return doc1

def create_vector_space_model2(all_words, thisline1, thisline2, thisline3):
	doc2 = []
	N = 3 #no of docs
	'''
	idf = log(N/df)
	W = (1 + log tf) * idf
	'''
	for i in all_words:
		tf=0
		df=0
		for j in range(0, len(thisline2)):
			if thisline2[j] == i:
				tf=tf+1
		if i in thisline1:
			df=df+1
		if i in thisline2:
			df=df+1
		if i in thisline3:
			df=df+1
		if(tf > 0):	
			term1 = 1 + math.log(tf,10)
		else:
			term1 = 0
		idf = math.log((N/df), 10)
		term2 = idf
		tf_idf = term1 * term2
		doc2.append(tf_idf)
	return doc2

def create_vector_space_model3(all_words, thisline1, thisline2, thisline3):
	doc3 = []
	N = 3 #no of docs
	'''
	idf = log(N/df)
	W = (1 + log tf) * idf
	'''
	for i in all_words:
		tf=0
		df=0
		for j in range(0, len(thisline3)):
			if thisline3[j] == i:
				tf=tf+1
		if i in thisline1:
			df=df+1
		if i in thisline2:
			df=df+1
		if i in thisline3:
			df=df+1
		if(tf > 0):	
			term1 = 1 + math.log(tf,10)
		else:
			term1 = 0
		idf = math.log((N/df), 10)
		term2 = idf
		tf_idf = term1 * term2
		doc3.append(tf_idf)
	return doc3
	
def find_cosine_similarity(doc1, doc2):
	dot_prod = d1 = d2 = 0
	for i in range(0, len(doc1)):
		dot_prod = dot_prod + doc1[i]*doc2[i]
	for i in range(0, len(doc1)):
		d1 = d1 + doc1[i]*doc1[i]
	for i in range(0, len(doc2)):
		d2 = d2 + doc2[i]*doc2[i]	
	sq1 = math.sqrt(d1)
	sq2 = math.sqrt(d2)
	return (dot_prod / (sq1*sq2))
	
f1 = open("1.txt", "r")
f2 = open("2.txt", "r")
f3 = open("3.txt", "r")

all_words = []
vector1=[]
vector2=[]
vector3=[]

line1 = f1.readlines()
for i in line1:
	thisline1= i.split(" ")
remove_newline(thisline1)
print("Tokenized Document 1 : ", thisline1)

line2 = f2.readlines()
for i in line2:
	thisline2= i.split(" ")
remove_newline(thisline2)
print("Tokenized Document 2 : ", thisline2)

line3 = f3.readlines()
for i in line3:
	thisline3= i.split(" ")
remove_newline(thisline3)
print("Tokenized Document 3 : ", thisline3)

construct_dataset(thisline1, thisline2, thisline3)
all_words = remove_duplicates(all_words)
print("Tokenized Dataset  : ",all_words)
	
vector1 = create_vector_space_model1(all_words, thisline1, thisline2, thisline3)
print("Vector for Document 1 : ", vector1)

vector2 = create_vector_space_model2(all_words, thisline1, thisline2, thisline3)
print("Vector for Document 2 : ", vector2)

vector3 = create_vector_space_model3(all_words, thisline1, thisline2, thisline3)
print("Vector for Document 3 : ", vector3)

print("Cosine Similarity between Document 1 and Document 2 : ",find_cosine_similarity(vector1, vector2))
print("Cosine Similarity between Document 1 and Document 3 : ",find_cosine_similarity(vector1, vector3))
print("Cosine Similarity between Document 2 and Document 3 : ",find_cosine_similarity(vector2, vector3))

