# 그래프경로
def dfs(S, V, G):
    visited = [0]*(V+1)
    st = []
    visited[S] = 1
    result = 0
    while True:
        for w in arr[S]:
            if visited[w] == 0:
                S = w
                st.append(S)
                visited[S] = 1
                break
        else:
            if st:
                S = st.pop()
            else: break
        if S == G:
            result = 1
            break
        else:
            result = 0
    return result

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S, V, G)}')
    
    


