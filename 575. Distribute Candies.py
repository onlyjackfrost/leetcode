class Solution:
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        #做多能拿多少種類 => 比較'姊姊做多能拿幾顆'和'有幾個種類'
        if int(len(candies)/2) >= len(set(candies)):
            return len(set(candies))
        else:
            return int(len(candies)/2)