def findErrorNums(nums):
    set_dict ={}
    len_nums = len(nums)
    for item in nums:
        try:
            set_dict[item] = 2
        except:
            set_dict[item] = 1
    missing_number = None 
    repeated_number = None 
    for number in range(1,len_nums+1):
        try: 
            if set_dict[number] ==2:
                repeated_number = number
        except:
            missing_number = number
    print(set_dict)
    return [repeated_number,missing_number]

if __name__ == '__main__':
    nums =[1,2,2,4]
    print(findErrorNums(nums))