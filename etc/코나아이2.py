
arr= [5,3,9,13]
num = 8;

def solution(arr,n):
  answer = []

  for i in range(0, len(arr) - 1):
    for n in arr[i + 1:]:
      s = arr[i] + n
      if not s in answer:
        answer.append(s)

  answer.sort()
  for i in range(0,len(arr)):
      if(answer[i] == num):
          return True;
      else:
          return False;

# def solution(arr,n):
#     for i in range(0, len(arr)):
#         for j in range(i+1,len(arr)):
#             ans = arr[i]+arr[j];
#
#     if(ans == n):
#         answer = True;
#     else:
#         answer = False;
#
#     return answer;
print(solution(arr,num))