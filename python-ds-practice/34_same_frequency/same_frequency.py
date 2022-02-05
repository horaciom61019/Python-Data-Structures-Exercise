def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    return freq_counter(num1) == freq_counter(num2)

def freq_counter(nums):
    counts = {}
    nums = str(nums)
    for x in nums:
        counts[x] = counts.get(x, 0) + 1

    return counts

print(same_frequency(551122, 221515))
print(same_frequency(321142, 3212215))
print(same_frequency(1212, 2211))