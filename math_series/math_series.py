def fibonacci(n, a1=0, a2=1):
    """
    This function receives a number representing the index of a number from the Fibonacci sequence.

    Parameters
    ----------
    n : int, required
      The index of the number in the sequence. 
    a1 : int, optional
      The first base value in the sequence.
      Default=0
    a2 : int, optional
      The second base value in the sequence.
      Default=1 

    Returns
    ------- 
    int
      The number in the Fibonacci sequence with the corresponding passed index.
    """
    nums = [a1, a2]
    for i in range(1, n):
        nums.append(nums[i-1] + nums[i])
    return nums[n]


def lucas(n, a1=2, a2=1):
    """
    This function receives a number representing the index of a number from the Lucas sequence.

    Parameters
    ----------
    n : int, required
      The index of the number in the sequence. 
    a1 : int, optional
      The first base value in the sequence.
      Default=2
    a2 : int, optional
      The second base value in the sequence.
      Default=1 

    Returns
    ------- 
    int
      The number in the Lucas sequence with the corresponding passed index.
    """
    nums = [a1, a2]
    for i in range(1, n):
        nums.append(nums[i-1] + nums[i])
    return nums[n]
