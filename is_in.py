# You are given two sets,  and .
# Your job is to find whether set  is a subset of set .

# If set  is subset of set , print True.
# If set  is not a subset of set , print False.

# Input Format

# The first line will contain the number of test cases, .
# The first line of each test case contains the number of elements in set .
# The second line of each test case contains the space separated elements of set .
# The third line of each test case contains the number of elements in set .
# The fourth line of each test case contains the space separated elements of set .

# Constraints

# Output Format

# Output True or False for each test case on separate lines.

# Sample Input

# 3
# 5
# 1 2 3 5 6
# 9
# 9 8 5 6 3 2 1 4 7
# 1
# 2
# 5
# 3 6 5 4 1
# 7
# 1 2 3 5 6 8 9
# 3
# 9 8 2
# Sample Output

# True 
# False
# False
# Explanation

# Test Case 01 Explanation

# Set  = {1 2 3 5 6}
# Set  = {9 8 5 6 3 2 1 4 7}
# All the elements of set  are elements of set .
# Hence, set  is a subset of set . 

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def is_in(a, b):
    
    for i in a:
        if i not in b: 
            return False
    return True 

print(is_in(a, b))