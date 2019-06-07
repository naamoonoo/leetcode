#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int	power(int base, int times)
{
	int res = 1;

	while (times-- > 0)
		res *= base;
	return (res);
}

int* powerfulIntegers(int x, int y, int bound, int* returnSize){
	int	*arr;
	int idx = 0;
	int counter = 0;

	arr = (int *)malloc(sizeof(int) * (bound + 1));
	for (int i = 0; i < bound + 1; i++)
		arr[i] = 0;
	for (int i = 0; power(x, i) <= bound; i++)
	{
		for (int j = 0; power(y, j) <= bound; j++)
		{
			if (power(x, i) + power(y, j) <= bound && !arr[power(x, i) + power(y, j)])
			{
				arr[power(x, i) + power(y, j)] = 1;
				counter++;
			}
		}
	}
	returnSize = (int *)malloc(sizeof(int) * counter);
	for (int i = 0; i < bound + 1; i++)
		if(arr[i])
			returnSize[idx++] = i;
	// for (int i = 0; i < counter; i++)
	// 	printf("%d ", returnSize[i]);
	return (returnSize);
}

int main()
{
	int *res = NULL;
	powerfulIntegers(2, 3, 10, res);

	return (0);
}
