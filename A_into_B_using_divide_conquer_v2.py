def multiplication(A,B):
    if B ==1:
        return A
    else:
        return A + multiplication(A,B-1)
if __name__ == '__main__':
    A = int(input('Enter A: '))
    B = int(input('Enter B: '))
    print(multiplication(A,B))