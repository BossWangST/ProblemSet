#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int maxValue(int n, int index, int maxSum) {
    long left, right;
    left = index;
    right = n - 1 - index;
    if (left > right) {
        long temp = left;
        left = right;
        right = temp;
    }
    long res1 =
        (double)(-(left - 0.5) + sqrt((left - 0.5) * (left - 0.5) -
                                      2 * (right + 1 - 0.5 * left * left -
                                           0.5 * left - maxSum)));
    long res2 = (double)(2 + sqrt(4 - 4 * (2 + left + right - maxSum))) / 2;
    long res3 = (double)(0.5 * left * left + 0.5 * right * right + 0.5 * left +
                        0.5 * right + maxSum) /
               (left + right + 1);
    if (res2 <= left + 1)
        return res2;
    else if (res1 > left + 1 && res1 <= right + 1)
        return res1;
    else if (res3 > right + 1)
        return res3;
    else
        return -1;
}
int main() {
    printf("%d\n", maxValue(3, 0, 815094800));
    return 0;
}

