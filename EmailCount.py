"""ead through the mbox-short.txt and figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer."""


name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts=dict()
for line in handle:
    line.rstrip()
    words=list()
    if line.startswith("From "):
        words=line.split()
        word=words[1]
        counts[word]=counts.get(word,0)+1  # get the value for the key "word" from the dict and add 1, if the key doesn't exist then get the value 0 and add 1 
        
 
bigword= "NONE"
bigcount= "NONE"
for word, count in counts.items():
    if bigcount == "NONE" or count > bigcount:
        bigword=word
        bigcount=count
print bigword, bigcount