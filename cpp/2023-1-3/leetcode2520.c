#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int countDigits(int num) {
    int cur;
    int ori = num;
    int res = 0;
    while (num > 0) {
        cur = num % 10;
        if (ori % cur == 0) res++;
        num /= 10;
    }
    return res;
}
int main() {
    printf("%d\n", countDigits(121));
    return 0;
}

