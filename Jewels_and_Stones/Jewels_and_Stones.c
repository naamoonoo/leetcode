#include <stdio.h>

int numJewelsInStones(char * J, char * S){
	int cnt;
	int i;
	int j;

	i = -1;
	cnt = 0;
	while (J[++i])
	{
		j = -1;
		while (S[++j])
		{
			if (J[i] == S[j])
				cnt++;
		}
	}
	return cnt;
}

int main()
{
	printf("%d\n", numJewelsInStones("aA", "aAAzzzwscxs"));
	return (0);
}
