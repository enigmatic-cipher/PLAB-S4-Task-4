"""
Given a string as input. Break the string in two halves and print them in following format. Assume string of even length.
Input-> "coding"
Output-> ing#coding#cod
"""

st = "coding"
ln = len(st)
st1 = ""
st2 = ""
pt = "#"
for i in range(ln//2,ln):
  ch = st[i]
  st1 = st1 + ch
for j in range(0,ln//2):
  ch2 = st[j]
  st2 = st2 + ch2
strn = st1 + pt + st + pt + st2
print(strn)
  