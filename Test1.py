#\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
#\b	Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain" r"ain\b"	
#\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain" r"ain\B"	
#\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
#\D	Returns a match where the string DOES NOT contain digits	"\D"	
#\s	Returns a match where the string contains a white space character	"\s"	
#\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
#\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
#\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
#\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# Python has a module named re to work with RegEx (Regular expressions)
import re

txt = "The rain in Spain"

#Check if "ain" is present at the beginning of a WORD:

x = re.findall(r"\bain", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")

#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):

x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
