#include <fstream>
#include <map>
#include <string>
#include <iterator>
using namespace std;

int main() {
    string rna;
    map<string, string>:: iterator rna_codon_itr;
    map<string, string> rna_codon = {
        {"UUU", "F"},    {"CUU", "L"}, {"AUU", "I"}, {"GUU", "V"},
        {"UUC", "F"},    {"CUC", "L"}, {"AUC", "I"}, {"GUC", "V"},
        {"UUA", "L"},    {"CUA", "L"}, {"AUA", "I"}, {"GUA", "V"},
        {"UUG", "L"},    {"CUG", "L"}, {"AUG", "M"}, {"GUG", "V"},
        {"UCU", "S"},    {"CCU", "P"}, {"ACU", "T"}, {"GCU", "A"},
        {"UCC", "S"},    {"CCC", "P"}, {"ACC", "T"}, {"GCC", "A"},
        {"UCA", "S"},    {"CCA", "P"}, {"ACA", "T"}, {"GCA", "A"},
        {"UCG", "S"},    {"CCG", "P"}, {"ACG", "T"}, {"GCG", "A"},
        {"UAU", "Y"},    {"CAU", "H"}, {"AAU", "N"}, {"GAU", "D"},
        {"UAC", "Y"},    {"CAC", "H"}, {"AAC", "N"}, {"GAC", "D"},
        {"UAA", "Stop"}, {"CAA", "Q"}, {"AAA", "K"}, {"GAA", "E"},
        {"UAG", "Stop"}, {"CAG", "Q"}, {"AAG", "K"}, {"GAG", "E"},
        {"UGU", "C"},    {"CGU", "R"}, {"AGU", "S"}, {"GGU", "G"},
        {"UGC", "C"},    {"CGC", "R"}, {"AGC", "S"}, {"GGC", "G"},
        {"UGA", "Stop"}, {"CGA", "R"}, {"AGA", "R"}, {"GGA", "G"},
        {"UGG", "W"},    {"CGG", "R"}, {"AGG", "R"}, {"GGG", "G"}
    };
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> rna;

    for (int i = 0; i < rna.length(); i += 3) {
        rna_codon_itr = rna_codon.find(rna.substr(i, 3));
        if (rna_codon_itr != rna_codon.end() && rna_codon_itr->second.compare("Stop") != 0)
            fout << rna_codon_itr->second;
    }
    fout << endl;
    fin.close();
    fout.close();

    return 0;
}
