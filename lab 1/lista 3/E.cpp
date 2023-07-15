#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare(const string& palavra1, const string& palavra2) {
    if (palavra1.length() < palavra2.length()) {
        return true;
    } else if (palavra1.length() > palavra2.length()) {
        return false;
    } else {
        return palavra1 < palavra2;
    }
}

int main() {
    
    string input;
    getline(cin, input);

    stringstream ss(input);
    string word;
    vector<string> line;

    while (ss >> word) {
        line.push_back(word);
    }

    sort(line.begin(), line.end(), compare);

    stringstream res;
    for (const string& x : line) {
        res << x << " ";
    }

    cout << res.str() << endl;
    return 0;
}