import math
class Solution(object):
	def twoSum(self, numbers, target):
		"""
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
		renum = []
		min = numbers[0]
		for i in range(0, len(numbers)):
			if numbers[i] > target-min: break
			else:
				for j in range(i+1, len(numbers)):
					if numbers[j] > target-min or (numbers[j] == numbers[i] and numbers[i] + numbers[j] != target): break
					else:
						if numbers[i] + numbers[j] == target:
							#renum = [orinumbers.index(numbers[i])+1, orinumbers.index(numbers[j])+1]
							renum = [i + 1, j + 1]
							return renum
	#binary search
	def twoSum2(self, numbers, target):
		for i in range(0, len(numbers)-1):
			renum = []
			low = i+1
			high = len(numbers)-1
			mid = (low+high) / 2
			while(low <= high):
				if numbers[i] + numbers[mid] == target:
					renum = [i + 1, mid + 1]
					return renum
				elif numbers[i] + numbers[mid] < target:
					low = mid + 1
				else: high = mid - 1
				mid = (low+high) / 2

s = Solution()
print s.twoSum2([2,3,4,4,9,56,90],8)