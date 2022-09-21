//수(num)와 배열을 입력받아 차례대로 num개의 요소만 포함된 새로운 배열을 리턴해야 합니다
#include <stdio.h>
#include <stdlib.h>
#pragma warning(disable:4996)


int printArray(int arr[], int count)    // 배열의 포인터와 요소의 개수를 받음
{



    if (len(arr) == count || count > len(arr)) return arr;
    else if (len(arr) == 0 || count == 0) return arr[0];



    return 1;


  
}


int main() {
    int numArr[10] = {-1, -2, 1, 2, 3, 4, 5};
//    int numArr[] = { 11, 22, 33, 44, 55, 66, 77, 88, 99, 110 };
    printArray(numArr, 5);
    //int arr[] = take(-1, -2, 1, 2, 3, 4, 5);
    
}
