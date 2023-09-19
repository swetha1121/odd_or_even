def conditionalSum(list1):
    even_count=0
    odd_count=0
    for i in range(len(list1)):
        if i%2==0:
            even_count+=list1[i]
        else:
            odd_count+=list1[i]
    return even_count,odd_count
list1=[1,2,3,4,5,6,7,8]
print(conditionalSum(list1))
