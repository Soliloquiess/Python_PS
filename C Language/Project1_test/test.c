/*
test.c
�����а� ���� �̸��� �ٸ� �� �ֽ��ϴ�.
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
		printf("%s �� %s �� ���� ���� �Դϴ�. \n", str1, str2);
	}
	else {
			printf("%s �� %s �� �ٸ� ���� �Դϴ�. \n", str1, str2);
	}
	return 0;
}

//#include <stdio.h>
//
//#pragma warning(disable:4996)
//char compare(char* str1, char* str2); //���� ������ �༭ str.c�� �ִ� compare�� �������� �Ǵ� ��
//
//int main() {
//	char str1[20];
//	char str2[20];
//	scanf("%s", str1);
//	scanf("%s", str2);
//	if (compare(str1, str2)) {
//		printf("%s �� %s �� ���� ���� �Դϴ�. \n", str1, str2);
//	}
//	else {
//		printf("%s �� %s �� �ٸ� ���� �Դϴ�. \n", str1, str2);
//	}
//	return 0;
//}