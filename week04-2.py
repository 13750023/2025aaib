#week04-2.py 是今天leetcode 挑戰題 easy 題(二合一)
#leetcode2529. maximum-count-of-positive-integer-and-negative-integer
#找出有幾個正數有幾個負數 大的那個要回傳
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0 #迴圈前面，準備好，都放0
        for i in range(len(nums)):#迴圈裡面更新他
            if nums[i]>0: pos+=1
            if nums[i]<0: neg+=1
        #迴圈後面，把答案拿來用
        return max(pos,neg)

