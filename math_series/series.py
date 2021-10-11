import math_series


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


def sum_series(idx, a1=0, a2=1):
    """
    This function receives a number representing the index of a number from a sequence. 
    If the optional parameters a1, a2 are not provided, the function will return the corresponding number from the Fibonacci sequence.
    If the optional parameters a1, a2 equal 2,1 respectively, the function will return the corresponding number from the Lucas sequence.
    Otherwise, the function will return the corresponding number from a sequence that starts with a1 and a2.

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
      The number in the resulting sequence with the specified index.
    """
    return fibonacci(idx) if a1 == 0 and a2 == 1 else lucas(idx) if a1 == 2 and a2 == 1 else fibonacci(idx, a1, a2)

if __name__ == "__main__":
  print(fibonacci(5))
  print(lucas(0))
  print(sum_series(10,10,20))