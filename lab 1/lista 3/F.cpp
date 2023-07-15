#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

bool is_match(const string& block1, const string& block2) {
    int i = 0;
    while (i <= 2) {
        if (block1[i] == block2[i]) {
            return false;
        }
        i++;
    }
    return true;
}

int main() {
    int amount, height, res = 0;
    cin >> amount >> height;
    string blocks[amount];

    for (int i = 0; i < amount; i++) {
        cin >> blocks[i];
    }

    vector<string> tower; 
    for (int i = 0; i < amount; i++) {
        bool match = false;

        string current = blocks[i];

        if (!tower.empty() && is_match(current, tower.back())) {
            match = true;
            tower.pop_back();
            res += 10;
        }

        if (!match) {
            if (tower.size() >= height) {
                cout << "game over" << endl;
                return 0;
            }

            tower.push_back(current);
        }
    }


    if (tower.size() != height) {
        cout << res << endl;
    } else {
        cout << "game over" << endl;
    }

    return 0;
}