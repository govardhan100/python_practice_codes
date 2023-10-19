def sum_up_n_numbers_v1(n):
    sum = 0
    while n>0:
        if n==1:
            sum+=1
            return sum
        else:
            sum+=n
            n-=1
    return sum 

def sum_up_n_numbers_v2(n):
    if n==1:
        return 1
    else:
        return n+sum_up_n_numbers_v2(n-1)
    


if __name__ =='__main__':
    num = int(input('Enter Number:'))
    print('method 1:',sum_up_n_numbers_v1(num))
    print("method 2:",sum_up_n_numbers_v2(num))