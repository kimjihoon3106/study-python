h, m = map(int, input().split())

if(h == 1 and m <45):
    h = 23
    m = 15 + m

print(h , m)