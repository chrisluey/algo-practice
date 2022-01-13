#include <unordered_map>
class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        std::unordered_map<char, int> hashMap;
        for (char& c: magazine) {
            if (hashMap.find(c) != hashMap.end()) {
                std::unordered_map<char, int>::iterator it = hashMap.find(c);
                it->second = it->second + 1;
            } else {
                hashMap[c] = 1;
            }
        }
        for (char& c: ransomNote) {
            if (hashMap.find(c) != hashMap.end()) {
                std::unordered_map<char, int>::iterator it = hashMap.find(c);
                if (it->second == 0) {
                    return false;
                }
                it->second = it->second - 1;
            } else {
                return false;
            }
        }
        return true;
    }
};