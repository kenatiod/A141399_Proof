// Exhaustive maximal prime support for consecutive p_r-smooth pairs, r <= 20.
// Compile: g++ -O3 -std=c++17 smooth_support_census.cpp -o smooth_support_census
// Run:     ./smooth_support_census > smooth_support_data.csv
// Uses exact published upper endpoints U_r = OEIS A002072(r), r <= 20.
// Check: counts must match OEIS A002071(r). No floating-point arithmetic.
#include <algorithm>
#include <cstdint>
#include <iostream>
using u64 = std::uint64_t;
constexpr int K=20;
constexpr int prime[K] = {2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71};
constexpr u64 U[K] = {
 1ULL,8ULL,80ULL,4374ULL,9800ULL,123200ULL,336140ULL,
 11859210ULL,11859210ULL,177182720ULL,1611308699ULL,
 3463199999ULL,63927525375ULL,421138799639ULL,
 1109496723125ULL,1453579866024ULL,20628591204480ULL,
 31887350832896ULL,31887350832896ULL,119089041053696ULL
};
u64 pairs[K]={}, best[K]={}, witness[K]={}, enumerated=0;
void enumerate(int j, u64 n, int n_support, int greatest_idx) {
    if (j==K) {
        ++enumerated;
        u64 remainder=n+1;
        int successor_support=0;
        int pair_greatest_idx=greatest_idx;
        for (int i=0; i<K; ++i) {
            if (remainder % prime[i] != 0) continue;
            ++successor_support;
            pair_greatest_idx=std::max(pair_greatest_idx,i);
            do {remainder/=prime[i];} while (remainder % prime[i] == 0);
        }
        if (remainder!=1) return; // n+1 is not p_20 smooth
        const int support=n_support+successor_support;
        for (int i=pair_greatest_idx; i<K; ++i) {
            if (n>U[i]) continue;
            ++pairs[i];
            if (support>best[i]) {best[i]=support;witness[i]=n;}
        }
        return;
    }
    for (u64 x=n; x<=U[K-1]; ) {
        enumerate(j+1, x, n_support+(x!=n),
                  (x==n ? greatest_idx : std::max(greatest_idx,j)));
        if (x>U[K-1]/prime[j]) break; // avoid overflow
        x*=prime[j];
    }
}
int main() {
    enumerate(0,1ULL,0,0);
    std::cerr << "Number of p_20-smooth n enumerated: " << enumerated << "\n";
    std::cout << "r,p_r,A002072_r,A002071_count,W_r,witness_m,support_fraction\n";
    for(int i=0;i<K;++i) {
        std::cout << i+1 << ',' << prime[i] << ',' << U[i] << ','
                  << pairs[i] << ',' << best[i] << ',' << witness[i] << ','
                  << double(best[i])/double(i+1) << '\n';
    }
}
