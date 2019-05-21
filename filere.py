import re 
# s=open("filere.txt",'r')
# line=s.read()
#pat=raw_input("enter the patterns to search: ")
line=intput("enter the input in which we have to find pattern")
pat= r"\b((?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.\b(?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.\b(?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.\b(?:1?[0-9]{1,2}|2[0-4][0-9]|25[0-5]))\b"
result=re.findall(pat,line)
print result



