import random

lower = "abvdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVMXYZ"
numbers = "0123456789"
symbols = "[]{}()*;/,.@$%#^&!>_<"

generatrisa = lower + upper + numbers + symbols
lenn = 16
password = "".join(random.sample(generatrisa, lenn))
print(password)