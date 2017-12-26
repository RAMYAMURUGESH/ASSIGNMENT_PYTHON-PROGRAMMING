#to count the no.of.upper case in the string using isupper() built in functions


s=input("ENTER THE STRING:")
count=0
for i in s:
	if i.isupper():
		count=count+1
print("THE NO.OF.CAPITAL LETTERS IN THE STRING:",s,count)

  
