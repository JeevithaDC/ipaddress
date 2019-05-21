import re 
# s=open("filere.txt",'r')
# line=s.read()
#pat=raw_input("enter the patterns to search: ")
line="PATTERN HOW jaVa 10.2.3.2 30.2.1.2 11111 12 0.0.0.1 345.1.1.1"
pat= r"\b((?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.\b(?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.\b(?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.\b(?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]))\b"
result=re.findall(pat,line)
print result



