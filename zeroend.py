arr = list(map(int,input().split()))
non_zero=[i for i in arr if i!=0]
zeros = [0]*(len(arr)-len(non_zero))
result = non_zero+zeros
print(result)
