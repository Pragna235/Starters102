# cook your dish here
for t in range(int(input())):
    x=int(input())
    commission = 0.2 * x 
    if(100 % commission == 0):
        print(int(100//commission))
    else:
        print(int((100//commission) + 1))
   