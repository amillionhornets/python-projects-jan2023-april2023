import re
"""
First the pattern will look for lowercase and uppercase letter and numbers before an @ symbol. 
Second, after the @ symbol the patter will look for any kind of letter.
Finally, .com, .edu, or .net will be searched for.
"""
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

userEmail = input("Email: ")

if(re.search(pattern, userEmail)):
    print("Valid")
else:
    print("Not Valid")