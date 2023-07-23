#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int countEven(int num) {
    if (num <= 10) {
        int res = 0;
        for (int i = 2; i < 10; i += 2)
            if (i <= num) res++;
        return res;
    }
    int level = num / 10;
    int digit = 0;
    int level_copy = level;
    while (level_copy > 0) {
        digit += level_copy % 10;
        level_copy /= 10;
    }
    int res = 5 * level - 1;
    if (digit % 2 != 0) {
        // even
        int max = level * 10 - 2 + 3;
        while (max <= num) {
            res++;
            max += 2;
        }
    } else {
        // odd
        int max = level * 10 - 1 + 1;
        while (max <= num) {
            res++;
            max += 2;
        }
    }

    return res;
}
int main() {
    printf("Hello world\n");
    return 0;
}

