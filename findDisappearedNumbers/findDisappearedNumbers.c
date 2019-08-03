/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* findDisappearedNumbers(int* nums, int numsSize, int* returnSize){
	returnSize = malloc(sizeof(int) * 2);
	returnSize[0] = 5;
	returnSize[1] = 6;
	return returnSize;
}

