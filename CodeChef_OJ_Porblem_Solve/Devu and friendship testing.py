# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))[:n]
    print(len(set(a)))
