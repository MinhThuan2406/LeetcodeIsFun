# 2182. Construct String With Repeat Limit

# Priority Queue (Max-Heap)
# Runtime: 32ms

# Complexity:
# + Time: O(k * log(n))
# + Space: O(n)

from collections import Counter
import heapq


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        # Max-heap: (-ord(ch), ch, count)
        max_heap = [(-ord(ch), ch, count) for ch, count in freq.items()]
        heapq.heapify(max_heap)

        result = []

        while max_heap:
            neg_ord, ch, count = heapq.heappop(max_heap)
            take = min(count, repeatLimit)
            result.append(ch * take)

            if count > repeatLimit:
                if not max_heap:
                    break
                neg_ord2, ch2, count2 = heapq.heappop(max_heap)
                result.append(ch2)
                if count2 > 1:
                    heapq.heappush(max_heap, (neg_ord2, ch2, count2 - 1))
                heapq.heappush(max_heap, (neg_ord, ch, count - repeatLimit))

        return "".join(result)
