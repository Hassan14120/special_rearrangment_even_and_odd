def special_rearrangement(nums):
    # Create two lists to hold even and odd numbers
    evens_nums = []
    odds_nums  = []
    for num in nums:
        if num % 2 == 0:
            evens_nums.append(num)
        else:
            odds_nums.append(num)
    return evens_nums + odds_nums

nums = [3, 1, 2, 4, 5, 6, 15, 21, 22, 23, 24, 25,]
result = special_rearrangement(nums)
print(result)  