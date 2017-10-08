#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

long long mortal_fibonnaci_rabbits(int month, int life) {
    vector<long long> rabbit_generations(life, 0);
    long long new_rabbits;

    // There is one pair of rabbit in the beginning
    rabbit_generations[0] = 1;

    for (int i = 1; i < month; i++) {
        // New pair of rabbits are born from matured rabbits
        new_rabbits = 0;
        for (int k = 1; k < life; k++)
            new_rabbits += rabbit_generations[k];

        // Rabbit pairs mature over a month
        for (int j = life - 1; j >= 1; j--) {
            rabbit_generations[j] = rabbit_generations[j - 1];
        }
        rabbit_generations[0] = new_rabbits;

        for (int k = 0; k < life; k++)
            cout << rabbit_generations[k] << " ";
        cout << endl;
    }

    long long mortal_rabbits = 0;
    for (int i = 0; i < life; i++)
        mortal_rabbits += rabbit_generations[i];

    return mortal_rabbits;
}

int main() {
    int n, m;
    cin >> n >> m;
    cout << mortal_fibonnaci_rabbits(n, m);

    return 0;
}
