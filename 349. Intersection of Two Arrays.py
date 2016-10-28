class Solution(object):
	def intersection(self, nums1, nums2):
		"""
		:type nums1: List[int]
		:type nums2: List[int]
		:rtype: List[int]
		"""
		a = set(nums1) & set(nums2)
		b = set(nums1).intersection(set(nums2))
		return list(set(nums1) & set(nums2))

	def intersect(self, nums1, nums2):
		head1 = 0
		head2 = 0
		nums1.sort()
		nums2.sort()
		n1 = len(nums1)
		n2 = len(nums2)
		res = []
		if nums1 ==  nums2: return nums1
		while (head1 < n1) and (head2 < n2):
			if nums1[head1] == nums2[head2]:
				res.append(nums1[head1])
				head1 += 1
				head2 += 1
				continue
			if nums1[head1] < nums2[head2]:
				head1 += 1
			else:
				head2 += 1
		return res
	def intersect2(self, nums1, nums2):
		res = []
		for num, count in (collections.Counter(nums1) & collections.Counter(nums2)).items():
			res += [num] * count
		return res

	def intersect3(self, nums1, nums2):
		table = {}
		res = []
		for i in nums1:
			table[i] = table.get(i, 0) + 1
		for j in nums2:
			if table.get(j) > 0:
				res.append(j)
				table[j] -= 1
		return res

s = Solution()
print s.intersect([2,1], [1,2])