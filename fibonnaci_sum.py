
def fibonnaci_sum_v1(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    return fibonnaci_sum_v1(n-1)+ fibonnaci_sum_v1(n-2)
def fibonnaci_sum_v2(n):
    current_fn = 0
    previous_fn = 1
    
    for i in range(0,n):
        if n == 0:
            return previous_fn
        if n == 1:
            return current_fn
        current_fn,previous_fn= current_fn+previous_fn,current_fn
    return current_fn 
if __name__=='__main__':
    number = int(input('Enter Number:'))
    print("Method 1: ",fibonnaci_sum_v1(number))
    print(f'Method 2:{fibonnaci_sum_v2(number)}')