def multiplication(A,B):
    sum = 0
    if A == 0 or B == 0:
        return 0

    while True:
        if B ==1:
            sum+= A
            return sum
        else:
            sum+= A
            B-=1
    return sum
if __name__ == '__main__':
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))

    print(multiplication(A,B))
    
