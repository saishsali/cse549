#include <map>
#include <string>
#include <iterator>
#include <fstream>
using namespace std;

map<string, int> get_amino_acid_frequency(map<string, string> rna_codon) {
    map<string, int> amino_acid_frequency;
    map<string, string> :: iterator rna_codon_itr;
    map<string, int> :: iterator amino_acid_frequency_itr;

    for (rna_codon_itr = rna_codon.begin(); rna_codon_itr != rna_codon.end(); rna_codon_itr++) {
        amino_acid_frequency_itr = amino_acid_frequency.find(rna_codon_itr->second);

        if (amino_acid_frequency_itr == amino_acid_frequency.end())
            amino_acid_frequency[rna_codon_itr->second] = 0;
        amino_acid_frequency[rna_codon_itr->second]++;
    }

    return amino_acid_frequency;
}

int main() {
    int num_RNA, modulo_base = 1000000;
    string protein;
    map<string, int> amino_acid_frequency;
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

    amino_acid_frequency = get_amino_acid_frequency(rna_codon);

    num_RNA = amino_acid_frequency["Stop"];
    fin >> protein;

    for (int i = 0; i < protein.length(); i++) {
        num_RNA *= amino_acid_frequency[string(1, protein[i])];

        if (num_RNA >= modulo_base)
            num_RNA %= modulo_base;
    }
    fout << num_RNA << endl;

    return 0;
}
