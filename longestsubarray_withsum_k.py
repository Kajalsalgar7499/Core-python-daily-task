arr = list(map(int,input().split()))
k= int(input())
prefix_sum=0
d={}
max_len=0
for i in range(len(arr)):
    prefix_sum+=arr[i]
    if prefix_sum ==k:
        max_len=i+1
    if prefix_sum - k in d:
        max_len=max(max_len,i-d[prefix_sum-k])
    if prefix_sum not in d:
        d[prefix_sum]=i
print(max_len)



