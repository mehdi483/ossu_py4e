# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below

name = input("Enter file: ")

try:
    handle = open(name)
except:
    print("Entered file name is not valid")
    quit()  

hours = dict()

for line in handle:
    if line.startswith("From "):
        words = line.rstrip().split()
        time = words[5]
        timeParts = time.split(":")
        hour = timeParts[0]
        hours[hour] = hours.get(hour, 0) + 1

for h, c in sorted(hours.items()):
    print(h, c)