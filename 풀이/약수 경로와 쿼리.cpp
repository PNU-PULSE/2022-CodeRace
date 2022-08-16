#include <bits/stdc++.h>
#define f first
#define s second
using namespace std;
int sv[3500000];
int gcd(int a, int b){
    int c;
    while (b != 0){
        c = a % b;
        a = b;
        b = c;
    }
    return a;
}
void preprocessing(){
    for (int i = 3; i <= 3500000; i += 2){
        if (sv[(i + 1) / 2] == 0) {
            sv[(i + 1) / 2] = i;
            int k = (i << 1);
            for (int j = i; j <= 3500000; j += k){
            	if (sv[(j + 1) / 2] == 0)	sv[(j + 1) / 2] = i;
            }
        }
    }
}
int main(){
    cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(false);
    memset(sv, 0, sizeof(sv));
    preprocessing();
    int q; cin >> q;
    while (q--){
        int a, b; cin >> a >> b;
        if ((b % a == 0) || (a % b == 0)) {
            cout << a << " " << b << "\n";
        }
        else if (a % 2 == 0 && b % 2 == 0){
            cout << a << " " << 2 << " " << b << "\n";
        }
        else if (a % 2 == 1 && b % 2 == 1){
            cout << a << " " << 1 << " " << b << "\n";
        }
        else{
            int p; p = gcd(a, b);
            if (p == 1){
                cout << a << " " << (long long int)a * (long long int)b << " " << b << "\n";
            }
            else{
                cout << a << " " << sv[(p + 1) / 2] << " " << b << "\n";
            }
        }
    }
}
