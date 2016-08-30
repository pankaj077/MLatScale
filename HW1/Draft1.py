#HW00

import os
os.chdir('/Users/z013sy0/Data science/Day 1/HW00')

#Question 1 

fhand =open("test.txt","r+")
fhand.close()
for word in fhand:
    print word
    
filename = "test.txt"

#All words- count
wordcount={} 
with open(filename) as file:
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

for word in wordcount:
    print word, wordcount[word]

#Just capital words- count
capwordcount={} 
with open(filename) as file:
    for word in file.read().split():
        if word[0].isupper():
            if word not in capwordcount:
                capwordcount[word] = 1
            else:
                capwordcount[word] += 1
        else:
            continue

for word in capwordcount:
    print word, capwordcount[word]

#Question 2
#20.8.1
letters='abcdefghijklmnopqrstuvwxyz'
letters = list(letters)

line = raw_input('Enter line\n')
line = line.lower()

lettercount={}
for word in line:
    for letter in word:
        if letter not in lettercount:
            lettercount[letter]=1
        else:
            lettercount[letter] += 1

for letter in letters:
    if letter in lettercount:
        print letter, lettercount[letter]

#20.8.2

d = {"apples": 15, "bananas": 35, "grapes": 12}
d["bananas"]
d["oranges"] = 20
len(d)
"grapes" in d
#d["pears"]
d.get("pears", 0)
fruits = list(d.keys())
fruits.sort()
print(fruits)
del d["apples"]
"apples" in d


def add_fruit(inventory, fruit, quantity=0):  
    if fruit not in inventory:
        inventory[fruit] =  quantity 
    else:
        inventory[fruit] +=  quantity 
    return inventory
 
new_inventory = {}
add_fruit(new_inventory, "strawberries", 10)

"strawberries" in new_inventory
if new_inventory["strawberries"] == 10:
    print "Yes\n"
add_fruit(new_inventory, "strawberries", 25)
if new_inventory["strawberries"] == 35:
    print "Yes\n"

#20.8.3
#write a text file with word counts and find number of alice

filename = "Alice.txt"
import re

wordcount={} 
with open(filename) as file:
    for line in file:
        clean_line = re.sub('\W+', " ",line )
        clean_line = clean_line.lower()
        words = clean_line.split()  
        for word in words:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
        

wc_key = list(wordcount.keys())
wc_key.sort()

#for word in wc_key:
#    print word, wordcount[word]
        
print wordcount["alice"]

#20.8.4
#find length of longest word
longest_length = 0
for word in wc_key:
    if len(word)>longest_length:
        longest_length = len(word)
        longest_word = word
    else:
        continue

print longest_word, longest_length

#re.sub('[^A-Za-z0-9]+', '', string)
