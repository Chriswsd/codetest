
def main():
    l = []
    n = 0
    while True:
        s = input()
        if ':' not in s:
            n = int(s)
            break
        else:
            a, b = s.split(':')
            a = int(a)
            l.append((a, b))
    
    l.sort()
    ans = ""

    for e in l:
        if n % e[0] == 0:
            ans += e[1]

    if ans == "":
        print(n)
    else:
        print(ans)
        

if __name__ == "__main__":
    main()