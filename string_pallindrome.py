#to check whether the given string is pallindrome or not .
#by using reversed() function the given string is reversed 


s1=input("ENTER THE STRING:")
s2=reversed(s1)
print (list(s2))
if list(s1) == list(s2):
	print("THE GIVEN STRING IS PALLINDROME")
else:
	print("THE GIVEN STRING IS NOT PALLINDROME")
