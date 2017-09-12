#include <fstream>
#include <map>
using namespace std;

int main() {
    int input_num = 0;
    string dna, intron, protein, line;
    map<string, char> dna_codon = {
        {"TTT", 'F'}, {"CTT", 'L'}, {"ATT", 'I'}, {"GTT", 'V'},
        {"TTC", 'F'}, {"CTC", 'L'}, {"ATC", 'I'}, {"GTC", 'V'},
        {"TTA", 'L'}, {"CTA", 'L'}, {"ATA", 'I'}, {"GTA", 'V'},
        {"TTG", 'L'}, {"CTG", 'L'}, {"ATG", 'M'}, {"GTG", 'V'},
        {"TCT", 'S'}, {"CCT", 'P'}, {"ACT", 'T'}, {"GCT", 'A'},
        {"TCC", 'S'}, {"CCC", 'P'}, {"ACC", 'T'}, {"GCC", 'A'},
        {"TCA", 'S'}, {"CCA", 'P'}, {"ACA", 'T'}, {"GCA", 'A'},
        {"TCG", 'S'}, {"CCG", 'P'}, {"ACG", 'T'}, {"GCG", 'A'},
        {"TAT", 'Y'}, {"CAT", 'H'}, {"AAT", 'N'}, {"GAT", 'D'},
        {"TAC", 'Y'}, {"CAC", 'H'}, {"AAC", 'N'}, {"GAC", 'D'},
        {"TAA", '#'}, {"CAA", 'Q'}, {"AAA", 'K'}, {"GAA", 'E'},
        {"TAG", '#'}, {"CAG", 'Q'}, {"AAG", 'K'}, {"GAG", 'E'},
        {"TGT", 'C'}, {"CGT", 'R'}, {"AGT", 'S'}, {"GGT", 'G'},
        {"TGC", 'C'}, {"CGC", 'R'}, {"AGC", 'S'}, {"GGC", 'G'},
        {"TGA", '#'}, {"CGA", 'R'}, {"AGA", 'R'}, {"GGA", 'G'},
        {"TGG", 'W'}, {"CGG", 'R'}, {"AGG", 'R'}, {"GGG", 'G'}
    };
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    while (getline(fin, line)) {
        if (line.compare(0, 10, ">Rosalind_") == 0) {
            input_num++;
        } else {
            if (input_num == 1) {
                dna += line;
            } else {
                intron = line;
                size_t pos = dna.find(intron);

                if (pos != string::npos)
                    dna.erase(pos, intron.length());
            }
        }
    }

    for (int i = 0; i < dna.length() - 3; i += 3) {
        protein += dna_codon[dna.substr(i, 3)];
    }

    fout << protein << endl;

    fin.close();
    fout.close();

    return 0;
}
