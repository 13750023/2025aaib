//week04-2.c �O���Ѫ�LeetCode �D���Deasy�D(�G�X�@)
//leetcode2529. maximum-count-of-positive-integer-and-negative-integer
int maximumCount(int* nums, int numsSize) {

    int pos=0,neg=0;//�j��e���A���O0
    for(int i=0;i<numsSize;i++){
        if(nums[i] > 0 )pos++; //����
        if(nums[i] < 0 )neg++; //�t��
    } //�j�餤���A��s�ק�L
    //�j��᭱�A�⥦���ӥ�
    if(pos>neg) return pos; //���Ƥ���h�A����
    else return neg; //���M�N�t��
}
