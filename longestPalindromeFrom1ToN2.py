import math
def createPalindrome(n):
    l = list(str(n*n))
    for i in range(0, len(l) // 2):
        # match the first part to the last part
        print(l[-1-i], l[i])
        l[-1-i] = l[i]
    nn = int("".join(l))
    if nn > n*n:
        # reduce the number before midpoint by 1
        nn = int( n*n - math.pow(10, (len(l)//2))  )
        l = list(str(nn))
        for i in range(0, len(l) // 2):
            # match the first part to the last part
            l[-1-i] = l[i]
    return int("".join(l))

if __name__ == "__main__":
    x = 10
    print(createPalindrome(x))