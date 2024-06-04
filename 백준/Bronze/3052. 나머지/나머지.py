def count_unique_remainders(numbers):
    # 각 숫자를 42로 나눈 나머지를 구함
    remainders = [num % 42 for num in numbers]
    #     for num in numbers:
    #         remainders.add(num % 42)
    # 서로 다른 나머지 값을 구함
    unique_remainders = set(remainders)
    # 서로 다른 나머지 값의 개수를 반환
    return len(unique_remainders)

# 10개의 숫자를 입력받음
numbers = []
for _ in range(10):
    num = int(input())
    numbers.append(num)

# 결과 출력
print(count_unique_remainders(numbers))

# def count_unique_remainders(numbers):
#     # 각 숫자를 42로 나눈 나머지를 구함
#     remainders = set()
#     for num in numbers:
#         remainders.add(num % 42)
#     # 서로 다른 나머지 값의 개수를 반환
#     return len(remainders)
#
# # 10개의 숫자를 입력받음
# numbers = []
# for _ in range(10):
#     num = int(input())
#     numbers.append(num)
#
# # 결과 출력
# print(count_unique_remainders(numbers))



# import java.util.HashSet;
# import java.util.Scanner;
#
# public class Main {
#     public static void main(String[] args) {
#         Scanner scanner = new Scanner(System.in);
#         HashSet<Integer> uniqueRemainders = new HashSet<>();
#
#         for (int i = 0; i < 10; ++i) {
#             int num = scanner.nextInt();
#             uniqueRemainders.add(num % 42);
#         }
#
#         System.out.println(uniqueRemainders.size());
#     }
# }

