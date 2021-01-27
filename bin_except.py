# Author: Adam Jeffries
# Date: 1/27/2021
# Description: Modifies the binary search function so that it returns "TargetNotFound"
# instead of -1.

class TargetNotFound(Exception):
    pass


def binary_search(a_list, target):
  """
  Searches a_list for an occurrence of target
  If found, returns the index of its position in the list
  If not found, returns -1, indicating the target value isn't in the list
  """
  first = 0
  last = len(a_list) - 1
  while first <= last:
    middle = (first + last) // 2
    if a_list[middle] == target:
      return middle
    if a_list[middle] > target:
      last = middle - 1
    else:
      first = middle + 1
    return TargetNotFound

def bin_except(num1, num2):
    try:
        result = int()
        print(result)
    except TargetNotFound:
        print("Target value not found.")
