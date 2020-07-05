#!/usr/bin/python3

def soma(*nums):
    #return nums
    #return type(nums)
    return sum(nums)

print(soma(6, 7, 5, 3, 52, 1))

def soma(nums):
    #return nums
    #return type(nums)
    return sum(nums)

nums = (6, 7, 5, 3, 52, 1)
print(soma(nums))