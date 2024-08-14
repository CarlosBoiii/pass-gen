from random import randint

# All uppercase password
password = ""
for i in range(8):
    i = chr(randint(65, 90))
    password = str(password) + i
print(password)

# Upper and lowercase password
password = ""
for i in range(4):
    i = chr(randint(65, 90))
    for j in range(4):
        j = chr(randint(65, 90)).lower()
    password = str(password) + i + j
print (password)



