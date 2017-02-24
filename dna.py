'''


'''

F = open("rosalind_dna.txt","r")
#print F.readlines() 
strand = F.read() 
#strand = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
#print strand
counterA = 0
counterC = 0
counterG = 0
counterT = 0
for symbol in strand:
    if symbol == "A":
        counterA = counterA + 1
    if symbol == "C":
        counterC = counterC + 1

    if symbol == "G":
        counterG = counterG + 1
    if symbol == "T":
           counterT = counterT + 1
print "Counter A %d" % (counterA)
print "Counter C %d" % (counterC)
print "Counter G %d" % (counterG)
print "counter T %d" % (counterT)
   

        
