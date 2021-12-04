#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <queue>

// This is pretty sloppy work, but it's 11:30 at night on a friday. It runs, it works, it could be better, but it will do.
int main()
{
    std::ifstream istream("./input1.txt");
    std::list<std::string> oxy_values;
    std::list<std::string> carbon_values;

    std::string temp;

    while (!istream.eof())
    {
        istream >> temp;
        oxy_values.push_back(temp);
        carbon_values.push_back(std::move(temp));
    }

    std::cout << "built list" << std::endl;

    int digit = 0;
    while (oxy_values.size() > 1)
    {
        int zeros = 0;
        int ones = 0;
        std::cout << "digit " << digit << std::endl;
        std::cout << "remaining " << oxy_values.size() << std::endl;
        for (const std::string &s : oxy_values)
        {
            if (s.at(digit) == '1')
            {
                ones++;
            }
            else
            {
                zeros++;
            }
        }
        std::cout << "ones: " << ones << " zeros: " << zeros << std::endl;
        char selector;
        if (ones >= zeros)
        {
            selector = '1';
        }
        else
        {
            selector = '0';
        }
        for (auto s = oxy_values.begin(); s != oxy_values.end(); s++)
        {
            if (s->at(digit) != selector)
            {
                s = oxy_values.erase(s);
                s--;
            }
        }
        digit++;
    }

    digit = 0;
    while (carbon_values.size() > 1)
    {
        int zeros = 0;
        int ones = 0;
        std::cout << "digit " << digit << std::endl;
        std::cout << "remaining " << carbon_values.size() << std::endl;
        for (const std::string &s : carbon_values)
        {
            if (s.at(digit) == '1')
            {
                ones++;
            }
            else
            {
                zeros++;
            }
        }
        char selector;
        if (ones >= zeros)
        {
            selector = '1';
        }
        else
        {
            selector = '0';
        }
        std::cout << "ones: " << ones << " zeros: " << zeros << std::endl;
        for (auto s = carbon_values.begin(); s != carbon_values.end(); s++)
        {
            if (s->at(digit) == selector)
            {
                s = carbon_values.erase(s);
                s--;
            }
        }
        digit++;
    }

    std::cout << "oxy: " << oxy_values.front() << " cabon: " << carbon_values.front() << std::endl;

    return 0;
}