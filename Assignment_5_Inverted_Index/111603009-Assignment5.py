#															IR ASSIGNMENT 3 
#																			Author - Shivam Milind Butale
#																			MIS - 111603009
#Python Program for Assignment 5 _ Inverted Index
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
f4 = open("4.txt", "r")
f5 = open("5.txt", "r")
f6 = open("6.txt", "r")

all_words = []

unique_words1 = set()
line1 = f1.readlines()
for i in line1:
	thisline1= i.split(" ")
	remove_newline(thisline1)
	for i in thisline1:
		unique_words1.add(i)
print("No of unique words in document 1: ", len(unique_words1))
print("\n")

unique_words2 = set()
line2 = f2.readlines()
for i in line2:
	thisline2= i.split(" ")
	remove_newline(thisline2)
	for i in thisline2:
		unique_words2.add(i)
print("No of unique words in document 2: ", len(unique_words2))
print("\n")

unique_words3 = set()
line3 = f3.readlines()
for i in line3:
	thisline3 = i.split(" ")
	remove_newline(thisline3)
	for i in thisline3:
		unique_words3.add(i)
print("No of unique words in document 3: ", len(unique_words3))
print("\n")

unique_words4 = set()
line4 = f4.readlines()
for i in line4:
	thisline4 = i.split(" ")
	remove_newline(thisline4)
	for i in thisline4:
		unique_words4.add(i)
print("No of unique words in document 4: ", len(unique_words4))
print("\n")

unique_words5 = set()
line5 = f5.readlines()
for i in line5:
	thisline5 = i.split(" ")
	remove_newline(thisline5)
	for i in thisline5:
		unique_words5.add(i)
print("No of unique words in document 5: ", len(unique_words5))
print("\n")

unique_words6 = set()
line6 = f6.readlines()
for i in line6:
	thisline6 = i.split(" ")
	remove_newline(thisline6)
	for i in thisline6:
		unique_words6.add(i)
print("No of unique words in document 6: ", len(unique_words6))
print("\n")

unique_words = set()
for i in unique_words1:
	unique_words.add(i)
for i in unique_words2:
	unique_words.add(i)
for i in unique_words3:
	unique_words.add(i)
for i in unique_words4:
	unique_words.add(i)
for i in unique_words5:
	unique_words.add(i)
for i in unique_words6:
	unique_words.add(i)

print("No of unique words : ", len(unique_words))
print("\n")	

for i in unique_words:
	list= []
	if i in unique_words1:
		list.append(1)
	if i in unique_words2:
		list.append(2)
	if i in unique_words3:
		list.append(3)
	if i in unique_words4:
		list.append(4)
	if i in unique_words5:
		list.append(5)
	if i in unique_words6:
		list.append(6)
	print(i,list)
