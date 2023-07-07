#include <iostream>
#include <vector>
#include <string>
#include <unordered_set>

using namespace std;

int main() {
    int n, m;  
    cin >> n;

    vector<string> especies;
    unordered_set<string> especies_ordered;
    especies.reserve(n);
    for (int i = 0; i < n; i++) {
        string x;
        cin >> x;
        especies.push_back(x);
        especies_ordered.insert(x);
    }

    vector<string> print;
    cin >> m;
    print.reserve(m);

    for (int i = 0; i < m; i++) {
        string x;
        cin >> x;
        if (especies_ordered.count(x)) {
            print.push_back(x + " vive!");
        } else {
            print.push_back(x + " foi extinto :(");
        }
    }

    for (const string& x : print) {
        cout << x << endl;
    }

    return 0;
}