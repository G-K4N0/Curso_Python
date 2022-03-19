import random
lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "012345679"
symbols = "[]{}()*;/,._-"

all = lower + upper + numbers + symbols
length = 24

password = "".join(random.sample(all,length))

print(password)