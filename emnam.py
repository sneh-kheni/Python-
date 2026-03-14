
def rec(arr,ans,i):
    if i==len(arr):
        print(ans)
        return
    ans.append(arr[i])
    rec(arr,ans,i+1)
    ans.pop()
    rec(arr,ans,i+1)




given = [1,2,3]
ans = []
freq = [False] * len(given)
ds = []
def permutations(given,ds,ans,freq):
    if len(ds)==len(given):
        ans.append(ds[:])
        return
    for i in range(len(given)):
        if not freq[i]:
            freq[i]=True
            ds.append(given[i])
            permutations(given,ds,ans,freq)
            ds.pop()
            freq[i]=False
permutations(given,ds,ans,freq)
print(ans)