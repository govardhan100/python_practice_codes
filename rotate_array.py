def rotate(nums,k):
    """
    Do not return anything, modify nums in-place instead.
    """
    len_nums = len(nums)
    k = k%len_nums
    temp_list = [0]*len(nums)
    for index, item in enumerate(nums):
        i=(index+k)%len_nums
        print(i)
        temp_list[i] = item
    print(temp_list)
    for index,item in enumerate(temp_list):
        nums[index] =item
    print(nums)
if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    rotate(nums,k)