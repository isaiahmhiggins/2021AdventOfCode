#include <iostream>
#include <fstream>
#include <vector>

int main()
{
    std::ifstream istream("./input1.txt");
    std::vector<int64_t> bit_count = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};

    std::string temp;

    while (!istream.eof())
    {
        istream >> temp;
        auto i = bit_count.begin();
        for (const char val : temp)
        {
            if (val == '1')
            {
                //increment val at i
                (*i)++;
            }
            //increment iterator location
            i++;
        }
    }

    int64_t gamma = 0;

    for (int64_t i : bit_count)
    {
        gamma = gamma << 1;
        if (i >= 500)
        {
            gamma = gamma | 0x1;
        }
    }

    int64_t epsilon = ~gamma & 0xFFF;

    for (int64_t i : bit_count)
    {
        std::cout << i << std::endl;
    }
    std::cout << "gamma: " << gamma << " epsilon: " << epsilon << " product: " << gamma * epsilon << std::endl;

    return 0;
}