#include <iostream>
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    int gcd(int n, int m) {
        int x1 = n <= m ? n : m;
        int x2 = n <= m ? m : n;
        int tmp;
        while (x1 > 0) {
            tmp = x2 % x1;
            x2 = x1;
            x1 = tmp;
        }
        return x2;
    }

    long long countPairs(vector<int>& nums, int k) {
        int counts[k+1];
        memset(counts, 0, sizeof counts);
        for (int i = 1; i < k; ++i) {
            if (k % i == 0) {
                for (auto num : nums) {
                    if (num % i == 0) {
                        ++counts[i]; 
                    }
                }
            }
        }
        for (auto num : nums) {
            if (num % k == 0) {
                ++counts[k];
            }
        }
        long long numPairs = 0;
        for (auto num : nums) {
            int d = gcd(num, k);
            int q = k / d;
            numPairs += counts[q];
            if (num % q == 0) {
                --numPairs;
            }
        }
        return numPairs / 2;
    }
};


int main() {
    return 0;
}

/*

#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <unordered_set>
#include <unordered_map>
#include <bitset>
#include <limits>
#include <iostream> 
#include <iomanip>  
#include <string>
#include <sstream>  
#include <algorithm>
#include <numeric>
#include <complex>
#include <functional>
#include <cstring>
#include <cmath>
#include <cassert>


#define INF              (int)1000000007
#define EPS              1e-9
#define pb               push_back
#define mp               make_pair
#define all(c)           c.begin(), c.end()
#define forall(i,a,b)    for(int i=a;i<(b);++i)
#define trav(a,x)        for(auto & a: x)
#define in(a,b)          ((b).find(a) != (b).end())
#define sz(c)            (int)(c).size()
#define input(a)         for(auto & x : a) cin >> x;

using namespace std;

typedef vector<int>      vi;
typedef pair<int,int>    ii;
typedef vector<vi>       vvi;
typedef vector<ii>       vii;
typedef long long        ll;

#ifdef DEBUG
#define trace(...)       __f(#__VA_ARGS__, __VA_ARGS__)
#define debug(args...)   {dbg,args; clog<<endl;}
#define print_( a )      for( auto & x : a ) clog << x << ' '; clog << '\n';
#define printPair_( a )  for( auto & x : a ) clog << '(' << x.first << ',' << x.second << ')' << ' '; clog << '\n';
#else
#define trace(...)       
#define debug(args...)            
#define print_( a )               
#define printPair_( a )           
#endif

struct debugger {
  template<typename T> debugger& operator , (const T& x) {    
    clog << x << " ";    return *this;    
  }
}dbg;

template <typename Arg1>
void __f(const char* name, Arg1&& arg1){
    cerr << name << ": " << arg1 << endl;
}

template <typename Arg1, typename... Args>
void __f(const char* names, Arg1&& arg1, Args&&... args){
    const char* comma = strchr(names + 1, ',');
    cerr.write(names, comma - names) << ": " << arg1 << " | ";
    __f(comma + 1, args...);
}

auto ____ =[]() { std::ios::sync_with_stdio(0); cin.tie(0); return nullptr; }();

class Solution {
public:
    vi primeFactors(int n)
    {
        vi ans;
        if(n%2==0)  ans.pb(2);
        while (n % 2 == 0) { n = n/2; }
    
        for (int i = 3; i <= sqrt(n); i = i + 2)
        {
            while (n % i == 0)
            {
                ans.pb(i);
                n = n/i;
            }
        }
        if (n > 2) ans.pb(n);
        return ans;
    }
    long long coutPairs(vector<int>& v, int k) {
        print_(v);
        trace(k);
        ll n = sz(v);
        if( k == 1 ) return n*(n-1)/2;
        vi prime_factors = primeFactors(k);
        trace("prime factors");
        print_(prime_factors);
        trace("prime factors");
        vi prime_factor_cnt;
        for(auto p : prime_factors){
            int tmp = 0, xx = k;
            while(xx%p==0){
                xx/=p;
                tmp++;
            }
            prime_factor_cnt.pb(tmp);
        }

        unordered_map<int,int> uniq_cnt;
        int m = sz(prime_factor_cnt);
        for(auto x: v){
            trace(x);
            int tmp = 1;
            forall(j,0,m){
                int p = prime_factors[j];
                int cnt_p = 0;
                if( x%p==0 ){
                    while(x%p==0 && cnt_p < prime_factor_cnt[j]){
                        x/=p;
                        tmp*=p;
                        cnt_p ++;
                    }
                }
            }
            trace(tmp);
            uniq_cnt[tmp] ++;
        }
        vector<pair<ll,ll>> w;
        for(auto p : uniq_cnt){
            w.pb(p);
        }
        trace("print pair");
        printPair_(w);
        trace("print pair");
        ll ans = 0;
        int mm = sz(w);
        forall(i,0,mm){
            if( w[i].first*w[i].first %k == 0){
                ans +=  w[i].second * (w[i].second -1)/2;
            }
            forall(j,i+1,mm){
                if( w[i].first * w[j].first % k == 0){
                    ans += w[i].second * w[j].second;
                }
            }
        }
        return ans;
    }
};
*/