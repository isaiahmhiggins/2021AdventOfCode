#include <iostream>
#include <fstream>
#include <vector>
#include <deque>

int main()
{
    std::ifstream istream("./input.txt");
    int64_t curr = 0;
    int64_t prev = 0;
    std::deque<int64_t> values;
    int64_t temp;
    for (size_t i = 0; i < 3; i++)
    {
        istream >> temp;
        values.push_back(temp);
        curr += temp;
    }
    prev = curr;

    int64_t increases = 0;

    while (!istream.eof())
    {
        int64_t temp;
        istream >> temp;
        values.push_back(temp);
        curr += temp;
        curr -= values.front();
        values.pop_front();
        if (curr > prev)
        {
            increases++;
        }
        prev = curr;
    }
    std::cout << increases << std::endl;
    return 0;
}