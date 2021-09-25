a = int(input())
b = int(input())

result = a
for i in map(int,input().split()):
    i = 0.01*i
    result = result + result*i
print("%.0f"%(result-a))

if result>a:
    print("good")
elif result==a:
    print("same")
elif result<a:
    print("bad")