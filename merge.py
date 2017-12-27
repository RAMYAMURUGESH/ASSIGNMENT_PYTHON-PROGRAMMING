#to print the upper case character of the merged string


s1="I Like C"
s2="Mary Likes Python"
s3= s1+s2
print(s3)
for i in range(len(s3)):
	if(s3[i].isupper()):
		print(s3[i])
		
	
