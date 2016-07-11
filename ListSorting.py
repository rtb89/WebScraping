name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
count=dict()
for line in handle:
    if line.startswith("From "):
        line.rstrip()
        words=line.split()
        word=words[5]
        time=word.split(":")
        hr= time[0]
        count[hr]= count.get(hr,0)+1
        

ls =list()
for (hr,count) in count.items():
    ls.append((hr,count))
    
ls.sort()

for (hr,count) in ls:
    print hr, count
    