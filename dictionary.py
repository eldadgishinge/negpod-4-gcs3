#changing romans into integers
s= input()  #declaring a  var x and put a string in it
def RomantoInterger(s):
  d= {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} # declaring the dictionary with roman numbers
  num=0
  for i in range(len(s)):
    if i+1 != len(s) and d[s[i]]<d[s[i+1]]:
      num = num - d[s[i]]
    else:
      num = num + d[s[i]]
  return num
      
      
print (RomantoInterger(s))
