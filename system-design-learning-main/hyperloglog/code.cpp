#include<bits/stdc++.h>
using namespace std;

class HyperLogLog {
private:
    int b;  // Number of bits usrd to select register
    int m;  // Number of registers = 2^b
    vector<int> reg;    // Registers

    // --------------------------
    // 64-bit hash function
    // --------------------------
    uint64_t hashValue(uint64_t x) {
        x += 0x9e3779b97f4a7c15ULL;

        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;

        x = (x ^ (x >> 27)) *
            0x94d049bb133111ebULL;

        x = x ^ (x >> 31);

        return x;
    }

    // -----------------------------
    // Calculate alpha constant
    // -----------------------------
    double getAlpha() {
        if(m == 16) return 0.673;
        if(m == 32) return 0.697;
        if(m == 64) return 0.709;
    }

    public:

    // --------------------------------
    // Constructor
    // b = number of bits used for register index
    //
    // Example:
    // b = 4
    // m = 2^4 = 16 registers
    // --------------------------------
    HyperLogLog(int b = 10) {
        this->b = b;
        m = 1 << b;
        reg.assign(m,0);
    }
};