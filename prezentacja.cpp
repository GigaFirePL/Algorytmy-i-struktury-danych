#include <iostream>
#include <vector>
#include <unordered_map>
#include <numeric>     // std::accumulate
#include <algorithm>   // remove_if, reverse

int main() {
    // 1. Lista ocen
    std::vector<int> grades = {5, 3, 8, 6, 2, 7, 4};

    // 2. Średnia
    double avg = static_cast<double>(
        std::accumulate(grades.begin(), grades.end(), 0)
    ) / grades.size();
    std::cout << "Average: " << avg << "\n";

    // 3. Filtrowanie <4
    grades.erase(
        std::remove_if(grades.begin(), grades.end(),
                       [](int g){ return g < 4; }),
        grades.end()
    );
    // grades: {5,8,6,7,4}

    // 4. Odwróć kolejność
    std::reverse(grades.begin(), grades.end());
    // grades: {4,7,6,8,5}

    // 5. Grupowanie
    std::unordered_map<std::string, std::vector<int>> cats;
    for (int g : grades) {
        std::string key = g < 4 ? "low"
                        : (g <= 6 ? "mid" : "high");
        cats[key].push_back(g);
    }

    // 6. Wypisz
    for (auto &kv : cats) {
        std::cout << kv.first << ": ";
        for (int x : kv.second) std::cout << x << " ";
        std::cout << "\n";
    }
    return 0;
}
