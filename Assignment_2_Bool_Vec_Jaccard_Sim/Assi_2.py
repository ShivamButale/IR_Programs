#															IR ASSIGNMENT 2 
#																			Author - Shivam Milind Butale
#																			MIS - 111603009
#Python Program for Assignment 2 - Read three documents, represent them in Boolean Vector Form, find jaccard similarity between the documents
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
	
def create_boolean_vector(all_words, thisline):
	boolean_vector = []
	for i in all_words:
		if i in thisline:
			boolean_vector.append(1)
		else:
			boolean_vector.append(0)
	return boolean_vector

def find_jaccard_similarity(thisline1, thisline2):
	a = set(thisline1)
	b=set(thisline2)
	c=a.intersection(b)
	return float(len(c)) / (len(a) + len(b) - len(c))
	
f1 = open("1.txt", "r")
f2 = open("2.txt", "r")
f3 = open("3.txt", "r")

all_words = []
boolean_vector = []
boolean_vector1=[]
boolean_vector2=[]
boolean_vector3=[]

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

boolean_vector1 = create_boolean_vector(all_words, thisline1)
print("Boolean Vector for Document 1 : ",boolean_vector1)

boolean_vector2 = create_boolean_vector(all_words, thisline2)
print("Boolean Vector for Document 2 : ",boolean_vector2)

boolean_vector3 = create_boolean_vector(all_words, thisline3)
print("Boolean Vector for Document 3 : ", boolean_vector3)

print("Jaccard Similarity between Document 1 and Document 2 : ",find_jaccard_similarity(thisline1, thisline2))
print("Jaccard Similarity between Document 1 and Document 3 : ",find_jaccard_similarity(thisline1, thisline3))
print("Jaccard Similarity between Document 2 and Document 3 : ",find_jaccard_similarity(thisline2, thisline3))
