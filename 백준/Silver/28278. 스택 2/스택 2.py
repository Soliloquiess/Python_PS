def main():
    import sys
    input = sys.stdin.readline  # 빠른 입력 처리
    stack = []
    result = []

    n = int(input().strip())  # 명령의 수

    for _ in range(n):
        command = input().strip()
        
        if command.startswith('1'):
            _, x = command.split()
            stack.append(int(x))
        elif command == '2':
            result.append(stack.pop() if stack else -1)
        elif command == '3':
            result.append(len(stack))
        elif command == '4':
            result.append(1 if not stack else 0)
        elif command == '5':
            result.append(stack[-1] if stack else -1)

    sys.stdout.write("\n".join(map(str, result)) + "\n")

if __name__ == "__main__":
    main()
