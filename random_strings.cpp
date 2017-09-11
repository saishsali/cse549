#include <iostream>
#include <string>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    int T, n;
    string dna;

    cout << fixed;
    cout << setprecision(3); // To print only 3 digits after decimal point
    cin >> T; // number of test cases

    while (T--) {
        cin >> dna >> n;
        double A[n], B[n];

        for (int i = 0; i < n; i++) {
            cin >> A[i]; // GC content
            B[i] = 0;

            for (int j = 0; j < dna.length(); j++) {
                if (dna[j] == 'G' || dna[j] == 'C')
                    B[i] += log10(A[i]/2);
                else if (dna[j] == 'A' || dna[j] == 'T')
                    B[i] += log10((1 - A[i])/2);
            }
        }

        for (int i = 0; i < n; i++) {
            cout << B[i] << " ";
        }
        cout << endl;
    }

    return 0;
}
