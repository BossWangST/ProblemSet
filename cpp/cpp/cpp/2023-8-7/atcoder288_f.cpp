//
//  atcoder288_f.cpp
//  cpp
//
//  Created by mac on 8/7/23.
//

#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<string.h>

#include <iostream>
#include <string>

using namespace std;

long long n, s;
string x;
long long M = 998244353;

long long func() {
    int i = 1;
    string cur = "" + x[0];
    long long p = 1;
    int k = 1 << (n - 2);
    while (k > 0) {
        if (s & k) {
            p *= stoi(cur) % M;
            cur = "" + x[i];
        } else {
            cur += x[i];
        }
        i++;
        k >>= 1;
    }
    return p * stoi(cur) % M;
}

int main(void) {
    cin >> n;
    cin >> x;
    s = 0;
    long long target = 1 << (n - 1);
    long long res = 0;
    while (s < target) {
        res += func();
        res %= M;
        s += 1;
    }
    printf("%lld", res);
    return 0;
}
