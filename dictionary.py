<<<<<<< HEAD
#changing romans into integers
=======
#!/usr/bin/python3
#This format prints integers after converting them from roman using dictionary
#A pyhton that converts romans into integers
>>>>>>> 282b4222403b4666a662593616179943fc43f377
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
