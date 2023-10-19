def factorial_computation_v1(A):
    if A==1:
        return 1
    else:
        return A*factorial_computation_v1(A-1)
    
def factorial_computation_v2(A):
    if A ==1:
        return 1
    total_result = 1
    for i in range(1,A+1):
        total_result= total_result*i
    return total_result

if __name__=='__main__':
    A = int(input('enter A:'))
    print("Method2:",factorial_computation_v2(A))
    print(f"Method1:{factorial_computation_v1(A)}")