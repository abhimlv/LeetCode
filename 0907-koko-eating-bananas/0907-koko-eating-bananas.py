class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low < high:
            mid =  (low + high)//2
            hrs = sum(math.ceil(pile/mid) for pile in piles)
            if hrs <= h:
                high = mid
            else:
                low = mid + 1
        return low