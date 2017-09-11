#include <iostream>
#include <string>
using namespace std;
#define SIZE 100

int dna_overlap(string s1, string s2) {
    int i, j, s1_len, s2_len, overlap;

    s1_len = s1.length();
    s2_len = s2.length();

    if (s1.compare(s1_len - 4, 4, s2, 0, 4) == 0) // Check for match of 4 or more characters
        return 0;

    if (s1.compare(s1_len - 3, 3, s2, 0, 3) == 0) // Check for match of 3 characters
        return 1;

    return 0;
}

void adjacency_list(string dna[], string rosalind[], int num_dna) {
    int overlap;

    for (int i = 0; i < num_dna; i++) {
        for (int j = 0; j < num_dna; j++) {
            if (i == j)
                continue;
            overlap = dna_overlap(dna[i], dna[j]);

            if (overlap == 1) {
                cout << rosalind[i] << " " << rosalind[j] << endl;
            }
        }
    }
}

int main() {
    int T, num_dna;
    string dna[SIZE], rosalind[SIZE];

    cin >> T; // number of test cases

    while (T--) {
        cin >> num_dna;

        for (int i = 0; i < num_dna; i++) {
            cin >> rosalind[i];
            cin >> dna[i];
        }

        adjacency_list(dna, rosalind, num_dna);
    }

    return 0;
}
