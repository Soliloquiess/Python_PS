str = input()
result = ""

for ch in str:
    if ch.isupper():
        result += ch.lower()
    else:
        result += ch.upper()

print(result)