nums = [1,2,3] #iteraable
inum =iter(nums) #iterator
while True:
    try:
        item = next(inum)
        print(item)

    except StopIteration:
        break