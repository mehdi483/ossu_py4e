name = input("Enter file: ")

try:
    handle = open(name)
except:
    print("Entered file name is not valid")
    quit()  

words = list()
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
