import heapq

def medianSlidingWindow(nums, k):
	small, large = [], []
	for i, x in enumerate(nums[:k]): 
		heapq.heappush(small, (-x,i))
	for _ in range(k-(k>>1)): 
		move(small, large)
	ans = [get_med(small, large, k)]
	for i, x in enumerate(nums[k:]):
		if x >= large[0][0]:
			heapq.heappush(large, (x, i+k))
			if nums[i] <= large[0][0]: 
				move(large, small)
		else:
			heapq.heappush(small, (-x, i+k))
			if nums[i] >= large[0][0]: 
				move(small, large)
		while small and small[0][1] <= i: 
			heapq.heappop(small)
		while large and large[0][1] <= i: 
			heapq.heappop(large)
		ans.append(get_med(small, large, k))
	return ans

def move(h1, h2):
	x, i = heapq.heappop(h1)
	heapq.heappush(h2, (-x, i))
	
def get_med(h1, h2, k):
	return h2[0][0] * 1. if k & 1 else (h2[0][0]-h1[0][0]) / 2.