void reverseString(char* s, int sSize){
	char tmp;

	for (int i = 0; i < sSize / 2; i++)
	{
		tmp = s[i];
		s[i] = s[sSize - i - 1];
		s[sSize - i - 1] = tmp;
	}
}

#include <stdio.h>
int main() {
	char a[] = "hello";
	 reverseString(a, 5);
	printf("%s\n",a);
	return(0);
}
