



class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        path = []
        n = len(candidates)
        self._dfs(candidates, 0, n, path, res, target)
        return res

    def _dfs(self, arr, begin, n, path, res, target):
        if target == 0:
            res.append(path[:])
            return

        for i in range(begin, n):
            if arr[i] > target:
                break
            if i > begin and arr[i] == arr[i-1]:
                continue
            path.append(arr[i])
            self._dfs(arr, i+1, n, path, res, target - arr[i])
            path.pop()

Solution().combinationSum2([1, 2, 3], 3)
