#include <string>
#include <fstream>
using namespace std;
#define SIZE 100

int string_overlap(string s1, string s2, string &combined) {
    int s1_len = s1.length(), s2_len = s2.length(), overlap_len = INT_MIN, i = 0, j = 0;

    if (s1_len > s2_len) {
        if (s1.find(s2) != string::npos) {
            combined = s1;

            return s2_len;
        } else {
            i = s1_len - s2_len;
        }
    } else if (s2_len > s1_len) {
        if (s2.find(s1) != string::npos) {
            combined = s2;

            return s1_len;
        } else {
            j = s2_len - s1_len;
        }
    } else {
        if (s1.compare(s2) == 0) {
            combined = s1;

            return s1_len;
        }
    }

    while (i < s1_len) {
        if (s1.compare(i, s1_len - i, s2, 0, s1_len - i) == 0) {
            overlap_len = s1_len - i;
            combined = s1 + s2.substr(overlap_len);
            break;
        }
        i++;
    }

    while (j < s2_len) {
        if (s2.compare(j, s2_len - j, s1, 0, s2_len - j) == 0) {
            if ((s2_len - j) > overlap_len) {
                overlap_len = s2_len - j;
                combined = s2 + s1.substr(overlap_len);
                break;
            }
        }
        j++;
    }

    return overlap_len;
}

string shortest_superstring(string dna[], int num_dna) {
    int i, j, overlap, max_overlap, max_left, max_right;
    string combined, max_combined;

    while (num_dna != 1) {
        max_overlap = INT_MIN;

        for (int i = 0; i < num_dna - 1; i++) {
            for (int j = i + 1; j < num_dna; j++) {
                overlap = string_overlap(dna[i], dna[j], combined);
                if (overlap > max_overlap) {
                    max_overlap = overlap;
                    max_combined = combined;
                    max_left = i;
                    max_right = j;
                }
            }
        }

        num_dna--;
        if (max_overlap == INT_MIN) {
            dna[0] += dna[num_dna];
        } else {
            dna[max_left] = max_combined;
            dna[max_right] = dna[num_dna];
        }
    }

    return dna[0];
}

int main() {
    int i = -1;
    string dna[SIZE], line;
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    while (getline(fin, line)) {
        if (line.compare(0, 10, ">Rosalind_") == 0) {
            i++;
        } else {
            dna[i] += line;
        }
    }

    fout << shortest_superstring(dna, i + 1) << endl;
    fin.close();
    fout.close();

    return 0;
}
