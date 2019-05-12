/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
#include <stdio.h>
#include <stdlib.h>

int numberOfLessThan(int target, int *nums, int numsSize)
{
	int i;
	int	count;

	i = 0;
	count = 0;
	while (i < numsSize)
		count += (nums[i++] <= target);
	return (count);
}

int *lessSet(int* nums, int numsSize, int target)
{
	int i;
	int idx;
	int count;
	int	*res;

	count = numberOfLessThan(target, nums, numsSize);
	res = (int *)malloc(sizeof(int) * count);
	i = -1;
	idx = 0;
	while (++i < numsSize)
		if (nums[i] <= target)
			res[idx++] = nums[i];
	return (res);
}

int* twoSum(int* nums, int numsSize, int target)
{
	int i;
	int size;

	i = 0;
	size = numberOfLessThan(target, nums, numsSize);
	while (i < size)
		printf("%d\n", lessSet(nums, numsSize, target)[i++]);
	// printf("%d\n", numberOfLessThan(target, nums, numsSize));
	return (NULL);
}


int main()
{
	int a[4] = {2, 7, 11, 15};
	int *res;
	res = twoSum(a, 4, 9);
	return (0);
}
