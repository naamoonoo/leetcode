#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int count_word(char *S);
int sumFromOneTo(int n);
int isVowel(char c);
char *ft_strdup(char *str, int idx, int is_last);
char **ft_silmple_split(char *S);
void	ft_swap(char *s, int last_idx);
void	print_append(int times, int is_last);


char* toGoatLatin(char* S) {
	char **splitted;
	char *temp;
	int	len;
	int i;

	splitted = ft_silmple_split(S);
	i = 0;
	len = 0;
	while (splitted[i])
		len += strlen(splitted[i++]);
	i = 0;
	temp = (char *)malloc(sizeof(char) * (len + 1));
	while (splitted[i])
		strcat(temp, splitted[i++]);
	while (splitted[i])
		free(splitted[i++]);
	free(splitted[0]);
	return (temp);
}

void	ft_swap(char *s, int last_idx)
{
	char temp;
	int i;

	i = -1;

	temp = s[0];
	while (++i < last_idx)
		s[i] = s[i + 1];
	s[i] = temp;
}

char **ft_silmple_split(char *S)
{
	char	**res;
	char	temp[4096];
	int		i;
	int		j;
	int		idx;

	res = (char **)malloc(sizeof(char *) * (count_word(S) + 1));
	i = -1;
	j = 0;
	idx = 0;
	while (S[++i])
	{
		if (S[i] == ' ')
		{
			temp[j] = '\0';
			res[idx] = ft_strdup(temp, idx, idx == (count_word(S)));
			idx++;
			j = 0;
		}
		else
			temp[j++] = S[i];
	}
	temp[j] = '\0';
	res[idx] = ft_strdup(temp, idx, idx == (count_word(S) - 1));
	res[++idx] = 0;
	return (res);
}

char *ft_strdup(char *str, int idx, int is_last)
{
	char	*res;
	int		i;

	if (!(res = (char *)malloc(sizeof(char) * (strlen(str) + (idx + 3) + 1))))
		return (NULL);
	i = -1;
	while (str[++i])
		res[i] = str[i];
	if (!isVowel(res[0]))
		ft_swap(res, i - 1);
	res[i++] = 'm';
	while (idx-- + 2)
		res[i++] = 'a';
	if (!is_last)
		res[i++] = ' ';
	res[i] = '\0';
	return (res);
}

int count_word(char *S)
{
	int i;
	int len;

	i = -1;
	len = 0;
	while (S[++i])
		if (S[i] == ' ')
			len++;
	return (len + 1);
}

int isVowel(char c)
{
	int i;

	i = -1;
	while ("aeiouAEIOU"[++i])
		if ("aeiouAEIOU"[i] == c)
			return (1);
	return (0);
}

#include <unistd.h>
int main()
{
	printf("%s\n",toGoatLatin("I speak Goat Latin"));
	// toGoatLatin("The quick brown fox jumped over the lazy dog");
	// while (1)
	// 	sleep(1);
	return (0);
}
