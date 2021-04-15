# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file: ")

try:
    handle = open(name)
except:
    print("Entered file name is not valid")
    quit()

senders = dict()

for line in handle:
    if line.startswith("From "):
        words = line.rstrip().split()
        sender = words[1]
        senders[sender] = senders.get(sender, 0) + 1

mostSender = None
mostSenderCount = None

for email,count in senders.items():
    if mostSender == None or count > mostSenderCount:
        mostSender = email
        mostSenderCount = count

print(mostSender, mostSenderCount)
