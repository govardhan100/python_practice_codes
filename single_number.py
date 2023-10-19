def singleNumber(nums ):
    temp_dict ={}
    for i in nums:
        try: 
            temp_dict[i]+=1
        except:
            temp_dict[i]=1 

    for i in temp_dict.keys():
        if temp_dict[i]!=2:
            return i
if __name__ =='__main__':
    nums =[2,2,1]
    print(singleNumber(nums))
