class TopKFrequentElements:
    """
    Desc:
        # 347
        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order. 
    Link: 
        https://leetcode.com/problems/top-k-frequent-elements/
    Notes:
        - use bucket 
    """

    # bucket sort - create countMap, create bucket list, iterate backwards thur bucket for k values
    # Time: O(n), n = length of nums
    # Space: O(n), n = length of nums
    def solution1(self, nums, k):
        res = []
        
        # create count map
        countMap = {}
        for n in nums: 
            countMap[n] = 1 + countMap.get(n, 0)

        # create frequence using bucket, idx is count, value is arr of nums with that count
        freq = [ [] for i in range(len(nums)+1) ]
        for num, cnt in countMap.items():
            freq[cnt].append(num)

        # get top k freq
        for i in range(len(freq)-1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    # using heap
    # Time: O(Nlogk)
    # Space: O(N+k)
    def solution2():
        pass