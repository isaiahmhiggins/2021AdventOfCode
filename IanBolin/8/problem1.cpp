#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

bool stringShorter(const std::string &a, const std::string &b)
{
    return a.size() < b.size();
}

void checkAndRemove(std::string &s, char c)
{
    auto loc = std::find(s.begin(), s.end(), c);
    if (loc != s.end())
    {
        s.erase(loc);
    }
}

int main()
{
    std::fstream pattern_file("input.1.txt");
    std::fstream value_file("input.2.txt");

    // std::fstream pattern_file("input.1.test.txt");
    // std::fstream value_file("input.2.test.txt");

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
        std::sort(patterns.begin(), patterns.end(), stringShorter);
        notes.emplace_back(std::make_pair(std::move(patterns), std::move(values)));
    }

    uint64_t sum = 0;
    for (auto &note : notes)
    {

        // Build segment map
        std::vector<char> segment_map = {' ', ' ', ' ', ' ', ' ', ' ', ' '};
        std::string one = note.first.at(0);
        std::string seven = note.first.at(1);
        std::string four = note.first.at(2);

        checkAndRemove(seven, one.front());
        checkAndRemove(seven, one.back());
        // segment a found
        segment_map.at(0) = seven.front();

        // find nine and segment g
        std::vector<std::string> NineSixZero = {note.first.at(6), note.first.at(7), note.first.at(8)};
        std::string nine;
        for (auto pattern : NineSixZero)
        {
            std::string string = pattern;
            checkAndRemove(string, one.front());
            checkAndRemove(string, one.back());
            checkAndRemove(string, seven.front());
            checkAndRemove(string, four.at(0));
            checkAndRemove(string, four.at(1));
            checkAndRemove(string, four.at(2));
            checkAndRemove(string, four.at(3));
            if (string.size() == 1)
            {
                // segment g found
                segment_map.at(6) = string.front();
                nine = pattern;
                std::cout << "nine: " << pattern << std::endl;
                break;
            }
        }

        // find zero and segment e
        std::string zero;
        for (auto pattern : NineSixZero)
        {
            std::string string = pattern;
            if (std::find(string.begin(), string.end(), one.front()) == string.end() || std::find(string.begin(), string.end(), one.back()) == string.end())
            {
                // six or nine
                continue;
            }
            for (auto letter : nine)
            {
                checkAndRemove(string, letter);
            }
            if (string.size() == 1)
            {
                // bottom character found
                segment_map.at(4) = string.front();
                zero = pattern;
                break;
            }
        }

        // find segment d
        std::string temp = nine;
        for (auto letter : zero)
        {
            checkAndRemove(temp, letter);
        }
        segment_map.at(3) = temp.front();

        // find segment b
        temp = four;
        checkAndRemove(temp, segment_map.at(3));
        checkAndRemove(temp, one.at(0));
        checkAndRemove(temp, one.at(1));
        segment_map.at(1) = temp.front();

        // find segment c
        temp = four;
        checkAndRemove(temp, segment_map.at(3));

        // find six
        std::string six;
        for (auto &string : NineSixZero)
        {
            if (string != nine && string != zero)
            {
                six = string;
                break;
            }
        }

        // find segment f
        temp = six;
        checkAndRemove(temp, segment_map.at(0));
        checkAndRemove(temp, segment_map.at(1));
        checkAndRemove(temp, segment_map.at(3));
        checkAndRemove(temp, segment_map.at(4));
        checkAndRemove(temp, segment_map.at(6));
        segment_map.at(5) = temp.front();

        // find segment c
        temp = one;
        checkAndRemove(temp, segment_map.at(5));
        segment_map.at(2) = temp.front();

        // Segment map complete

        for (auto i : segment_map)
        {
            std::cout << i << std::endl;
        }

        // build value map
        std::vector<std::string> values = {"", "", "", "", "", "", "", "", "", ""};
        //segment a belongs to
        char segment_a = segment_map.at(0);
        values.at(0).push_back(segment_a);
        values.at(2).push_back(segment_a);
        values.at(3).push_back(segment_a);
        values.at(5).push_back(segment_a);
        values.at(6).push_back(segment_a);
        values.at(7).push_back(segment_a);
        values.at(8).push_back(segment_a);
        values.at(9).push_back(segment_a);

        //segment b belongs to
        char segment_b = segment_map.at(1);
        values.at(0).push_back(segment_b);
        values.at(4).push_back(segment_b);
        values.at(5).push_back(segment_b);
        values.at(6).push_back(segment_b);
        values.at(8).push_back(segment_b);
        values.at(9).push_back(segment_b);

        //segment c belongs to
        char segment_c = segment_map.at(2);
        values.at(0).push_back(segment_c);
        values.at(1).push_back(segment_c);
        values.at(2).push_back(segment_c);
        values.at(3).push_back(segment_c);
        values.at(4).push_back(segment_c);
        values.at(7).push_back(segment_c);
        values.at(8).push_back(segment_c);
        values.at(9).push_back(segment_c);

        //segment d belongs to
        char segment_d = segment_map.at(3);
        values.at(2).push_back(segment_d);
        values.at(3).push_back(segment_d);
        values.at(4).push_back(segment_d);
        values.at(5).push_back(segment_d);
        values.at(6).push_back(segment_d);
        values.at(8).push_back(segment_d);
        values.at(9).push_back(segment_d);

        //segment e belongs to
        char segment_e = segment_map.at(4);
        values.at(0).push_back(segment_e);
        values.at(2).push_back(segment_e);
        values.at(6).push_back(segment_e);
        values.at(8).push_back(segment_e);

        //segment f belongs to
        char segment_f = segment_map.at(5);
        values.at(0).push_back(segment_f);
        values.at(1).push_back(segment_f);
        values.at(3).push_back(segment_f);
        values.at(4).push_back(segment_f);
        values.at(5).push_back(segment_f);
        values.at(6).push_back(segment_f);
        values.at(7).push_back(segment_f);
        values.at(8).push_back(segment_f);
        values.at(9).push_back(segment_f);

        //segment g belongs to
        char segment_g = segment_map.at(6);
        values.at(0).push_back(segment_g);
        values.at(2).push_back(segment_g);
        values.at(3).push_back(segment_g);
        values.at(5).push_back(segment_g);
        values.at(6).push_back(segment_g);
        values.at(8).push_back(segment_g);
        values.at(9).push_back(segment_g);

        for (auto &value : values)
        {
            std::sort(value.begin(), value.end());
        }

        uint64_t output = 0;
        for (auto &string : note.second)
        {
            output *= 10;
            std::sort(string.begin(), string.end());
            for (int i = 0; i < 10; i++)
            {
                if (string == values.at(i))
                {
                    output += i;
                    break;
                }
            }
        }
        sum += output;
    }

    std::cout << sum << std::endl;

    return 0;
}