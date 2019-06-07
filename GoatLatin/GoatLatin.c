#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char	*str_handle(char *input)
{
	char tmp;
	for (int i = 0; i < (int)strlen(input) - 1; i++)
	{
		tmp = input[i];
		input[i] = input[i + 1];
		input[i + 1] = tmp;
	}
	return (input);
}

char	*str_join(char *res, char *input, int counter)
{
	char *tmp = malloc(sizeof(char) * ((res ? strlen(res) + 1 : 0) + strlen(input) +
		2 + counter + 1));
	if (res)
	{
		tmp = strcpy(tmp, res);
		tmp = strcat(tmp, " ");
		tmp = strcat(tmp, !strchr("aeiouAEIOU", input[0]) ? str_handle(input) : input);
	}
	else
		tmp = strcpy(tmp, !strchr("aeiouAEIOU", input[0]) ? str_handle(input) : input);
	tmp = strcat(tmp, "ma");
	while (counter--)
		tmp = strcat(tmp, "a");
	tmp[strlen(tmp)] = '\0';
	res = strdup(tmp);
	free(tmp);
	return res;
}

char* toGoatLatin(char * S){
	char	*ptr = strtok(S, " ");
	char	*res = NULL;
	char	*tmp;
	int		counter = 1;

	while (ptr != NULL)
	{
		tmp = str_join(res, ptr, counter++);
		res ? free(res) : 0;
		res = strdup(tmp);
		free(tmp);
		ptr = strtok(NULL, " ");
	}
	return res;
}

#include <unistd.h>
int main()
{
	char st[] = "I speak Goat Latin";
	printf("%s\n",toGoatLatin(st));
	char str[] = "The quick brown fox jumped over the lazy dog";
	printf("%s\n",toGoatLatin(str));
	char stc[] = "Each word consists of lowercase and uppercase letters only";
	printf("%s\n",toGoatLatin(stc));

	// while (1)
	// 	sleep(1);
	return 0;
}
// int main()
// {
// 	printf("%s\n",toGoatLatin("I speak Goat Latin"));
// 	// toGoatLatin("The quick brown fox jumped over the lazy dog");
// 	// while (1)
// 	// 	sleep(1);
// 	return (0);
// }
