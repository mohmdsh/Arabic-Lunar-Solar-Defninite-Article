

# ----*Introduction*----, 
'''
The consonants of Arabic are divided into two groups
on the basis of their effect on the definite article (al). Fourteen of them are
classified as “sun” letters by the criterion of assimilation of the preceding
 definite article. The assimilation occur in the liquid sound of the definite article (l). The word “shams” meaning ‘sun’ begins with one of 
the fourteen letters that trigger such assimilation. The term 'sun' is clearly non-phonetic but is almost
equivalent to 'dental/alveolar', 'apical', and 'coronal' sounds. 
Note that the affricate (dg) is not a “sun” consonant. The rest of the consonants, which are 14,  
called moon letters, do not assimilate with the liquid sound of the definite article.

----*The assumption*----
Broadly speaking, the assumtion that the assimilation process will make Arabic speakers to produce the moon consonants
faster than sun consonants because they include no assimilation process. Thus, they are more frequenct than 
the sun consonants.

----*The purpose of this project*----

This little code looks into a written Arabic corpus from different Arabic news agencies. 
The main purpose of it is to extract  the frequency of words that have definite artice followed by either moon & sun consonants.
Then, it compares the ratio of the both kinds in the whole copus to the ratio of the same kinds in the dictionary constructed in this code.

----*Some definitions*----
t(Word Token) means the presence of a word in a corpus.
(Word Type) means the presence of a word in a constructed dictionary made in an application.
'''

# -*- coding: utf-8 -*- #
# regular expression, codecs for reading Arabic
# reuqest, zipfile, io, to read a website downoload a zipfile, extract zipfile
# beautifulsoup for reading html from downloaded files
import re
import codecs
import requests, zipfile, io
import os
from bs4 import BeautifulSoup, Doctype

# import the corpus from a website. download and extract the zipfile 
url = 'https://sourceforge.net/projects/arabiccorpus/files/latest/download'

# download ziple file from the url
r = requests.get(url)
z = zipfile.ZipFile(io.BytesIO(r.content))
# unzip the file in z 
z.extractall()

#read the files since they are all html-type.
def readFile(fileName):
    with open(fileName) as f:
        soup = BeautifulSoup(f.read(),'html.parser')
        x = soup.get_text()

        # search for any word that has a definite article.
        wordtokens = re.findall(r'\bال\w+\b', x, re.U)
        return wordtokens

# store all the tokens in  corpus_tokens
corpus_tokens = []

# read in all subfolders and start counting the tokens in the corpus.
for root, dirs, files in os.walk(".", topdown=False):
    for fileHTML in files:
        if fileHTML.endswith('.html'):
            fname = os.path.join(root, fileHTML)
            corpus_tokens += readFile(fname)

# make a set of the corpus_tokens
wordtypes = set(corpus_tokens)

# identify the moon consonants 
moonsegments = u'أإآابحجخعىء'

# identify the sun consonants
sunsegments = u' تثدذرزسشصضطظلن'

# start a counter for tokens for both types of consonants
mooncounter_tokens = 0 
suncounter_tokens = 0 

# find token frequency by looping
for token in corpus_tokens:
	#if the consonant preceeding the definite article in moonsegement, then
	#increment the count in mooncounter.
	if token[2] in moonsegments:
		mooncounter_tokens +=1
	#if the consonant preceeding the definite article in sunsegement, then
	#increment the count in suncounter.
	if token[2] in sunsegments:
		suncounter_tokens+=1

print ('----*Results*----')
print ('In this corpus, the number of words that have the definite article followed by moon consonants is', ':',mooncounter_tokens, '\n')
print  ('In this corpus, the number of words that have the definite article followed by sun consonants is', ':',suncounter_tokens, '\n')    

# for type frequency for moon & sun consonants 
mooncounter_types = 0
suncounter_types = 0 

# # find type frequency by looping
for token in wordtypes:

	#if the consonant preceeding the definite article in moonsegement, then
	#increment the count in mooncounter_type.
	if token[2] in moonsegments:
		mooncounter_types+=1
        
	#if the consonant preceeding the definite article in moonsegement, then
	#increment the count in mooncounter_type.
	if token[2] in sunsegments:
		suncounter_types+=1
print ('In the construsted dictionary, the total number of words that have definite article followed by a moon segment is : ', mooncounter_types,'\n')
print ('In the construsted dictionary, the total number of words that have definite article followed a sun segment is : ', suncounter_types, '\n')

# prvide the length of wordtypes and store in a variable
totalType = len(wordtypes)
print ('The total number of word type is : ', totalType,  '\n')

#count the ratio of the moon segment in types
moonTypeFreq = (1.0 * mooncounter_types/totalType) * 100
print ('The ratio of the moon segments in terms of type is :', moonTypeFreq, '\n')

#count the ratio of the sun segment in types
sunTypeFreq = (1.0 * suncounter_types/totalType) * 100
print ('The ratio of the sun segments in terms of type is :', sunTypeFreq, '\n')

# provide the length of wordtokens to get the ratio
totalToken = len(corpus_tokens)
print ('The total number of word tokens is :',totalToken, '\n')

# count the ratio of the moon segment in tokens
moonTokenFeq = (1.0 * mooncounter_tokens/totalToken) * 100
print ('The ratio of the moon segments in terms of token is : ', moonTokenFeq, '\n')
#count the ratio of the sun segment in tokens
sunTokenFrq = (1.0 * suncounter_tokens/totalToken) * 100
print ('The ratio of the sun segments in terms of token is : ',sunTokenFrq, '\n')
