class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) -1 # 전체 후보

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            elif nums[mid] < target: # 가운데가 더 작으면 오른쪽에 있ㄷ
                l = mid + 1
            else:
                r = mid - 1
        return -1

