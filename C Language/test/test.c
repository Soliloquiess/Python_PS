/*
test.c
여러분과 파일 이름은 다를 수 있습니다.
*/

/* test.c */
#include <stdio.h>
#include "str.h" 

#pragma warning(disable:4996)
int main() {
	char str1[20];
	char str2[20];
	scanf("%s", str1);
	scanf("%s", str2);
	if (compare(str1, str2)) {
		printf("%s 와 %s 는 같은 문장 입니다. \n", str1, str2);
	}
	else {
			printf("%s 와 %s 는 다른 문장 입니다. \n", str1, str2);
	}
	return 0;
}

//#include <stdio.h>
//
//#pragma warning(disable:4996)
//char compare(char* str1, char* str2); //여기 선언해 줘서 str.c에 있는 compare를 가져오게 되는 것
//
//int main() {
//	char str1[20];
//	char str2[20];
//	scanf("%s", str1);
//	scanf("%s", str2);
//	if (compare(str1, str2)) {
//		printf("%s 와 %s 는 같은 문장 입니다. \n", str1, str2);
//	}
//	else {
//		printf("%s 와 %s 는 다른 문장 입니다. \n", str1, str2);
//	}
//	return 0;
//}