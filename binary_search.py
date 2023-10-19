def binary_search(start_index,end_index,nums,target):
    print(start_index,end_index)
    if start_index ==end_index:
        return start_index
    if (end_index - start_index ) ==1:
        if nums[end_index] == target:
            return end_index
        if nums[start_index] == target:
            return start_index
        else:
            return end_index


    mid = int(start_index+end_index)//2
    if nums[mid] == target :
        return mid
    if nums[mid]> target:
        return binary_search(start_index,mid,nums,target)
    else:
        return binary_search(mid,end_index,nums,target) 

if __name__ =='__main__':   
    nums = [1,3,5,6]

    print(binary_search(0,len(nums)-1,nums,7))