# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

count = 0.0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    
    zeroIndex = line.find("0")
    numStr = line[zeroIndex:]
    num = float(numStr)
    
    count += 1
    total += num

print("Average spam confidence:",total / count)