from collections import deque

#BFS 메서드 정의
def bfs(graph, start, visited):
    #큐(Queue) 구혀능ㄹ 위해 deque라이브러리 사용
    queue = deque([start]);
    #현재 노드를 방문처리
    visited[start] = True;
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v= queue.popleft();
        print(v,end=' ');
        #해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i);
                visited[i] = True;
#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],   #인덱스 0 부분은 빈 리스트로 넣어주는 것이 좋다.
  [2, 3, 8],    #1번 인덱스에 인접한 노드는 뭔지
  [1, 7],       #2번 인덱스에 인접한 노드는 뭔지
  [1, 4, 5],    #3번 인덱스에 인접한 노드는 뭔지
  [3, 5],       #4번 인덱스에 인접한 노드는 뭔지
  [3, 4],       #5번 인덱스에 인접한 노드는 뭔지
  [7],          #6번 인덱스에 인접한 노드는 뭔지
  [2, 6, 8],    #7번 인덱스에 인접한 노드는 뭔지
  [1, 7]        #8번 인덱스에 인접한 노드는 뭔지
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9   #여기서 인덱스 0은 사용하지 않음 그래서 8이 아닌 9를 사용했다.

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)