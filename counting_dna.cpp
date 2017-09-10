#include <iostream>
using namespace std;

int main() {
    int T, arr[4] = {0};
    string dna;

    cin >> T;
    while (T--) {
        cin >> dna;

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

        for (int i = 0; i < 4; i++)
            cout << arr[i] << " ";

        cout << endl;
    }

    return 0;
}
