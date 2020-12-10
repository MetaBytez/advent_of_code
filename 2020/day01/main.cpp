#include <fstream>
#include <iostream>
#include <set>
#include <string>

using namespace std;

int part_1(set<int> numbers) {
    int delta;
    for (set<int>::iterator num=numbers.begin(); num != numbers.end(); num++) {
        delta = 2020 - (*num);
        if (numbers.find(delta) != numbers.end()) {
            return delta * (*num);
        }
    }
    return -1;
}

int part_2(set<int> numbers) {
    int delta_1, delta_2;

    for (set<int>::iterator i = numbers.begin(); i != numbers.end(); i++) {
        delta_1 = 2020 - (*i);

        for (set<int>::iterator j = numbers.begin(); j != i; j++) {
            delta_2 = delta_1 - (*j);

            if ( numbers.find(delta_2) != numbers.end() && numbers.find(delta_2) != i ) {
                return (*i) * (*j) * delta_2;
            }
        }
    }
    return -1;
}

int main() {
    string line;
    set<int> numbers;
    ifstream inputFile ("input.txt");

    while ( getline(inputFile, line) ) { numbers.insert(stoi(line)); }
    inputFile.close();

    cout << part_1(numbers) << endl;
    cout << part_2(numbers) << endl;

    return 0;
}
