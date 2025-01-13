N = int(input())  # 설문조사한 사람 수

cute_count = 0
for _ in range(N):
    if int(input()) == 1:
        cute_count += 1

if cute_count > N / 2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")


#N = int(input())  
#votes = [int(input()) for _ in range(N)] 

# 1의 개수를 셈
#cute_count = votes.count(1)

#if cute_count > N // 2:
#    print("Junhee is cute!")
#else:
#    print("Junhee is not cute!")
