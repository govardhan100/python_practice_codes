def plusOne_v1(digits):
    carry = 1
    for i in range(len(digits)-1,-1,-1):
        digits[i],carry= (digits[i]+carry)%10,(digits[i]+carry)//10    
    if carry:
        #print(carry,digits)
        return [carry]+digits
    return digits
def get_carry(digits,i):
    if len(digits)==0:
        return 0

    if i==(len(digits)-1):
        carry,digits[i]=(digits[i]+1)//10, (digits[i]+1)%10
        return carry
    else:
        temp_carry = get_carry(digits,i+1)
        carry,digits[i]=(digits[i]+temp_carry)//10, (digits[i]+temp_carry)%10
        return carry
def plusOne_v2(digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=get_carry(digits,0)
        if carry == 1:
            return [carry]+digits
        else:
            return digits
if __name__ =='__main__':
    #print(plusOne([9]))
    print(plusOne_v2([9]))
    print(plusOne_v1([9]))

    print(plusOne_v2([4,3,2,1]))
    print(plusOne_v1([4,3,2,1]))
