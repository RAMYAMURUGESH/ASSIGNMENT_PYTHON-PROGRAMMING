#to print the reversal of the resultant string.
#the resutant string is obtained by encountering the characters at the even position of the given string.

s=input("ENTER THE STRING:")
s1=""
for i in range(len(s)):
	if i%2 == 0:
		s1=s1+s[i]
	
print("THE CHARACTERS AT THE EVEN POSITION OF THE STRING :",s1)
s2=reversed(s1)
print("THE REVERSAL OF CHARACTERS FROM THE RESULTANT STRING IS:",list(s2))
