# view
for tc in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    cnt = 0
    for i in range(2,N-2):
        if heights[i-2] < heights[i] and heights[i-1] < heights[i] and heights[i+1] < heights[i] and heights[i+2] < heights[i]:
            cnt += (heights[i] - max(heights[i-2], heights[i-1], heights[i+1], heights[i+2]))
    print(f'#{tc} {cnt}')
