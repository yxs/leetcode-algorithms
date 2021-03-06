import heapq


# heap sort 使用python内建堆
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or not k or k < 0:
            return None
        minheap = []
        for num in nums:
            if len(minheap) < k:
                heapq.heappush(minheap, num)
            else:
                if num > minheap[0]:
                    heapq.heappushpop(minheap, num)
        return minheap[0]


#  quick select
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # convert the kth largest to smallest
        # 第 k 个最大即升序的 len(nums) + 1 - k
        return self.findKthSmallest(nums, len(nums) + 1 - k)

    def findKthSmallest(self, nums, k):
        if nums:
            pos = self.partition(nums, 0, len(nums) - 1)
            if k > pos + 1:
                return self.findKthSmallest(nums[pos + 1 :], k - pos - 1)
            elif k < pos + 1:
                return self.findKthSmallest(nums[:pos], k)
            else:
                return nums[pos]

    # choose the right-most element as pivot
    def partition(self, nums, l, r):
        low = l
        while l < r:
            if nums[l] < nums[r]:
                nums[l], nums[low] = nums[low], nums[l]
                low += 1
            l += 1
        nums[low], nums[r] = nums[r], nums[low]
        return low
