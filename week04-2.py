#week04-2.py �O����leetcode �D���D easy �D(�G�X�@)
#leetcode2529. maximum-count-of-positive-integer-and-negative-integer
#��X���X�ӥ��Ʀ��X�ӭt�� �j�����ӭn�^��
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos=0
        neg=0 #�j��e���A�ǳƦn�A����0
        for i in range(len(nums)):#�j��̭���s�L
            if nums[i]>0: pos+=1
            if nums[i]<0: neg+=1
        #�j��᭱�A�⵪�׮��ӥ�
        return max(pos,neg)

