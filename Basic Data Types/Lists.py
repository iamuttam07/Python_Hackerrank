if __name__ == '__main__':
    N = int(input())
    res= []
    for i in range(0,N):
        a= input().split(" ")
        cmd = a[0]
        if cmd == 'append':
            res.append(int(a[1]))
        elif cmd == 'print':
            print(res)
        elif cmd == 'insert':
            res.insert(int(a[1]), int(a[2]))
        elif cmd == 'reverse':
            res.reverse()
        elif cmd == 'pop':
            res.pop()
        elif cmd == 'sort':
            res= sorted(res)
        elif cmd == 'remove':
            res.remove(int(a[1]))
