N = int(input())

weight = []
for i in range(N):
    W = int(input())
    weight.append(W)

weight.sort(reverse=True)
for i in range(N):
    weight[i] = weight[i] * (i+1)

print(max(weight))


    
    

