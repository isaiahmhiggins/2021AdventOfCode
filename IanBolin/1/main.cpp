#include <iostream>
#include <fstream>
#include <vector>

int main()
{
    std::ifstream istream("./input.txt");
    int64_t curr = 0;
    int64_t prev = 0;
    istream >> curr;
    prev = curr;

    int64_t increases = 0;

    while (!istream.eof())
    {
        istream >> curr;
        if (curr > prev)
        {
            increases++;
        }
        prev = curr;
    }
    std::cout << increases << std::endl;
    return 0;
}