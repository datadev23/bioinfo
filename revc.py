'''
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
is the string sc formed by reversing the symbols of s

, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s

of length at most 1000 bp.

Return: The reverse complement sc
of s.


'''
#read in the file

F = open("rosalind_revc.txt","r")
revc = F.read() 
# reverse the string
#revc = 'AAAACCCGGT'
index = -1
reverse = (revc[::-1])
print reverse

reversedlist = list(reverse)
print reversedlist

# convert a string to a list
reversedlist = list(reverse)

print reverse

for i in reversedlist:
    index = index + 1
    print index
    #print i
    if i == "T":
        reversedlist[index] = "A"
    if i == "A":
        reversedlist[index] = "T"
    if i == "G":
        reversedlist[index] = "C"
    if i == "C":
        reversedlist[index] = "G"    
          
print reversedlist
    #convert the list back to a string
rnastring = ''.join(reversedlist)
print rnastring

#ouput the data to a textfile called rosalind_revc_results.txt
recvoutput = open("rosalind_revc_results.txt", "w")
recvoutput.write(rnastring)
recvoutput.close()





    
    
        
        







