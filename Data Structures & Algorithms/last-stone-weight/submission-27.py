class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            heaviest,other = -heapq.heappop(stones),-heapq.heappop(stones)
            if heaviest > other: heapq.heappush(stones, -(heaviest - other))
        stones.append(0)
        return -stones[0]