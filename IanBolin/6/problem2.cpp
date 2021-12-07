#include <vector>
#include <list>
#include <iostream>
#include <fstream>

int main()
{
    std::vector<uint64_t> fish_by_age = {0, 0, 0, 0, 0, 0, 0, 0, 0};

    // std::ifstream input("input.test.txt");
    std::ifstream input("input.transformed.txt");
    while (!input.eof())
    {
        int64_t fish_age = -1;
        input >> fish_age;
        std::cout << fish_age << std::endl;
        fish_by_age.at(fish_age)++;
    }

    const int64_t num_days = 256;
    // const int64_t num_days = 80;
    // const int64_t num_days = 18;
    for (int64_t i = 0; i < num_days; i++)
    {
        uint64_t baby_fish = fish_by_age.at(0);
        uint64_t reset_fish = fish_by_age.at(0);
        for (int8_t j = 0; j < 8; j++)
        {
            fish_by_age.at(j) = fish_by_age.at(j + 1);
        }
        fish_by_age.at(8) = baby_fish;
        fish_by_age.at(6) += reset_fish;
    }
    uint64_t num_fishes = 0;
    for (uint64_t fish : fish_by_age)
    {
        num_fishes += fish;
    }
    std::cout << "On day " << num_days << " there are " << num_fishes << " fish" << std::endl;

    return 0;
}