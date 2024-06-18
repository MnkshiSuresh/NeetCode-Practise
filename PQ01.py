#There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

#Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

#Note that multiple kids can have the greatest number of candies.

from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    maximum = max(candies)
    return [(candy + extraCandies) >= maximum for candy in candies]
        
        
candies = [12,1,12]
extraCandies = 1
print(kidsWithCandies(candies, extraCandies))
