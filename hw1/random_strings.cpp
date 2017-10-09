#include <fstream>
#include <string>
#include <cmath>
#include <iomanip>
using namespace std;
#define SIZE 20

int main() {
    int n, i = 0;
    string dna;
    double A[SIZE], B[SIZE];
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fout << fixed;
    fout << setprecision(3); // To print only 3 digits after decimal point

    fin >> dna;

    while (fin >> A[i]) {
        B[i] = 0;

        for (int j = 0; j < dna.length(); j++) {
            if (dna[j] == 'G' || dna[j] == 'C')
                B[i] += log10(A[i]/2);
            else if (dna[j] == 'A' || dna[j] == 'T')
                B[i] += log10((1 - A[i])/2);
        }
        i++;
    }
    n = i;

    for (i = 0; i < n; i++) {
        fout << B[i];
        if (i != n - 1)
            fout << " ";
    }
    fout << endl;

    fin.close();
    fout.close();

    return 0;
}
