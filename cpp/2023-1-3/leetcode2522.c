#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
long long sub(char* s, long long l, long long r) {
    long long res = 0;
    long long mul = 1;
    for (long long i = r; i >= l; i--) {
        res += (s[i] - '0') * mul;
        mul *= 10;
    }
    return res;
}
int minimumPartition(char* s, long long k) {
    long long l = 0, r = 0;
    long long len = strlen(s);
    long long cur;
    long long res = 0;
    while (l < len && r < len) {
        cur = sub(s, l, r);
        if (cur > k) return -1;
        while (cur <= k && r < len) cur = sub(s, l, ++r);
        res++;
        l = r;
    }
    return res;
}
int main() {
    printf("%d\n", minimumPartition("1", 1));
    return 0;
}

