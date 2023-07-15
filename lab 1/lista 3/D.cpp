#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

string search_for(vector<pair<string, int>>* file, const string& book) {

    int left = 0, right = file -> size() - 1;


    bool found = false;

    
    while (right >= left) {
        int mid = left + (right - left) / 2;

        if ((*file)[mid].first == book) {
            if ((*file)[mid].second == 1) {
                found = true;
                return "Disponivel";
            } else {
                found = true;
                return "Emprestado";
            }
        } else if ((*file)[mid].first > book) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    if (!found) {
        return "Nao encontrado";
    }
}

int main() {
    vector<pair<string, int>> dictionary;
    int amount, status, n;
    cin >> amount;


    for (n = 0; n < amount; n++) {
        string code;
        cin >> code >> status;

        dictionary.push_back(make_pair(code, status));
    }



    int amount2;
    cin >> amount2;

    sort(dictionary.begin(), dictionary.end());




    for (n = 0; n < amount2; n++) {
        string book;
        cin >> book;

        string res = search_for(&dictionary, book);
        cout << res << endl;
    }

    return 0;
}
