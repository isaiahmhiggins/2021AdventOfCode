#include <fstream>
#include <iostream>
#include <vector>

int main()
{
    std::fstream pattern_file("input.1.txt");
    std::fstream value_file("input.2.txt");

    std::vector<std::pair<std::vector<std::string>, std::vector<std::string>>> notes;
    while (!pattern_file.eof())
    {
        std::string temp;
        std::vector<std::string> patterns;
        std::vector<std::string> values;

        for (int i = 0; i < 10; i++)
        {
            pattern_file >> temp;
            patterns.emplace_back(std::move(temp));
        }

        for (int i = 0; i < 4; i++)
        {
            value_file >> temp;
            values.emplace_back(std::move(temp));
        }
        notes.emplace_back(std::make_pair(std::move(patterns), std::move(values)));
    }

    std::vector<std::vector<std::pair<std::vector<std::string>, std::vector<std::string>>>::iterator> ones;
    std::vector<std::vector<std::pair<std::vector<std::string>, std::vector<std::string>>>::iterator> fours;
    std::vector<std::vector<std::pair<std::vector<std::string>, std::vector<std::string>>>::iterator> sevens;
    std::vector<std::vector<std::pair<std::vector<std::string>, std::vector<std::string>>>::iterator> eights;

    int64_t count = 0;
    for (auto note = notes.begin(); note != notes.end(); note++)
    {
        bool save_ones = false;
        bool save_fours = false;
        bool save_sevens = false;
        bool save_eights = false;
        for (const auto &val : note->second)
        {
            if (val.size() == 2)
            {
                save_ones = true;
                count++;
            }
            else if (val.size() == 3)
            {
                save_sevens = true;
                count++;
            }
            else if (val.size() == 4)
            {
                save_fours = true;
                count++;
            }
            else if (val.size() == 7)
            {
                save_eights = true;
                count++;
            }
        }
    }
    std::cout << count << std::endl;
}