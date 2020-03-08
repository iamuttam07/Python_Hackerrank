if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    num=set(arr)
    li=sorted(list(num))
    print(li[-2])

