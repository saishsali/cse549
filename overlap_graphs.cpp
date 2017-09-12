#include <fstream>
#include <string>
using namespace std;
#define SIZE 100

int dna_overlap(string s1, string s2, int k) {
    int i, j, s1_len, s2_len, overlap;

    s1_len = s1.length();
    s2_len = s2.length();

    if (s1.compare(s1_len - (k + 1), k + 1, s2, 0, k + 1) == 0) // Check for match of 4 or more characters
        return 0;

    if (s1.compare(s1_len - k, k, s2, 0, k) == 0) // Check for match of 3 characters
        return 1;

    return 0;
}

void adjacency_list(string dna[], string rosalind[], int num_dna, int k) {
    int overlap;
    ofstream fout("output.txt");

    for (int i = 0; i < num_dna; i++) {
        for (int j = 0; j < num_dna; j++) {
            if (i == j)
                continue;
            overlap = dna_overlap(dna[i], dna[j], k);

            if (overlap == 1) {
                fout << rosalind[i] << " " << rosalind[j] << endl;
            }
        }
    }
    fout.close();
}

int main() {
    int num_dna, k = 3, i = -1;
    string dna[SIZE], rosalind[SIZE], line;
    ifstream fin("input.txt");

    while (getline(fin, line)) {
        if (line.compare(0, 10, ">Rosalind_") == 0) {
            i++;
            rosalind[i] = line.substr(1);
        } else {
            dna[i] += line;
        }
    }

    adjacency_list(dna, rosalind, i + 1, k);
    fin.close();

    return 0;
}
