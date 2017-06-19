persons = {\
	"ab:cd:ef:12:34:56" : "John Smith", \
	"78:90:ab:cd:ef:12" : "David Smith"}

scanresults = open('scanresult.txt', 'r')
personshome = open('personshome.txt', 'w')

for line in scanresults:
    words = line.split()
    for word in words:
        # word is either an IP or a MAC
        if word in persons:
            personshome.write(persons[word]+'\n')
            #print persons[word]
