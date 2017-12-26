#to count the no.of.vowels in the string


s=input("ENTER THE STRING:")
count=0
for t in s:
	if(t=='a' or t=='e' or t=='i' or t=='o' or t=='u' or t=='A' or t=='E' or t=='I' or t=='O' or t=='U'):
		count=count+1
print("THE NO.OF.VOWELS IN THE GIVEN STRING IS ",s,count)
