#include <iostream>
#include <fstream>
using namespace std;
#define SIZE 4

int main() {
    int arr[SIZE] = {0};
    string dna;
    ifstream fin("input.txt");
    ofstream fout("output.txt");

    fin >> dna;

    for (int i = 0; i < dna.length(); i++) {
        if (dna[i] == 'A')
            arr[0]++;
        else if(dna[i] == 'C')
            arr[1]++;
        else if (dna[i] == 'G')
            arr[2]++;
        else if (dna[i] == 'T')
            arr[3]++;
    }

    for (int i = 0; i < SIZE; i++)
    {
        fout << arr[i];
        if (i != SIZE - 1)
            fout << " ";
    }

    fout << endl;

    return 0;
}
