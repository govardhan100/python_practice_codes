def binary_presentation(n):
    if n ==0:
        return [0]
    if n ==1:
        return [1]
    else:
        return binary_presentation(n//2)+[n%2]
if __name__ =='__main__':
    print(binary_presentation(10))