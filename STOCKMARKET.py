# cook your dish here
for t in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    total=sum(arr)
    mini=min(arr)
   
    print(total-mini)