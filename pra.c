#include<stdio.h>
int main() {
    int arr[] = {4,5,0,1,9,0,5,0};
    int n = 8, i, count = 0;

    for(i = 0; i < n; i++) {
        if(arr[i] != 0) {
            arr[count++] = arr[i];
        }
    }

    while(count < n) {
        arr[count++] = 0;
    }

    for(i = 0; i < n; i++)
        printf("%d ", arr[i]);

    return 0;
}