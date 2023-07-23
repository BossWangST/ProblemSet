//
// Created by mac on 1/7/23.
//


#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<string.h>

char *categorizeBox(int length, int width, int height, int mass) {
    unsigned long long vol = (unsigned long long) length * (unsigned long long) width * (unsigned long long) height;
    bool flag1, flag2;
    flag1 = flag2 = false;
    if (length >= 1e4 || width >= 1e4 || height >= 1e4 || vol >= 1e9)
        flag1 = true;
    if (mass >= 100)
        flag2 = true;
    if (flag1 && flag2)
        return "Both";
    else if (!flag1 && !flag2)
        return "Neither";
    else if (flag1 && !flag2)
        return "Bulky";
    else
        return "Heavy";
}

int main(void) {
    printf("Hello World\n");
    return 0;
}
