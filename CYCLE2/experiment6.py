#AIM :Store a list of first names. Count the occurrences of ‘a’ within the list.

names=['hiranya','anmaria','dhaksh','arsha','antony']
c=0
for word in names:
  c+=word.lower().count('a')
print(c)
