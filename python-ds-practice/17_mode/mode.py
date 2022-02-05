from itertools import count


def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    counter ={}

    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    max_value = max(counter.values())

    for (num, freq) in counter.items():
        if freq == max_value:
            return num

print(mode([1, 2, 1]))
print(mode([2, 2, 3, 3, 2]))