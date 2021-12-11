#include <iostream>
#include <fstream>
#include <stack>
#include <queue>

int64_t score_char(char c)
{
    int64_t val = 0;
    if (c == '(')
    {
        val = 1;
    }
    else if (c == '[')
    {
        val = 2;
    }
    else if (c == '{')
    {
        val = 3;
    }
    else if (c == '<')
    {
        val = 4;
    }

    return val;
}

int main()
{
    std::ifstream input("input.txt");
    std::priority_queue<int64_t> scores;
    while (!input.eof())
    {
        std::string line;
        input >> line;
        std::stack<char> opening;
        bool invalid = false;
        for (auto loc : line)
        {
            if (loc == '(' || loc == '[' || loc == '{' || loc == '<')
            {
                opening.push(loc);
            }
            else
            {
                char last_open = opening.top();
                opening.pop();
                if (last_open == '(' && loc != ')')
                {
                    invalid = true;
                    break;
                }
                else if (last_open == '[' && loc != ']')
                {
                    invalid = true;
                    break;
                }
                else if (last_open == '{' && loc != '}')
                {
                    invalid = true;
                    break;
                }
                else if (last_open == '<' && loc != '>')
                {
                    invalid = true;
                    break;
                }
            }
        }
        std::cout << opening.size() << " " << invalid << std::endl;
        if (!invalid)
        {
            int64_t score = 0;
            while (!opening.empty())
            {
                score *= 5;
                score += score_char(opening.top());
                opening.pop();
            }
            if (score != 0)
            {
                scores.emplace(score);
            }
            std::cout << score << std::endl;
        }
    }
    int64_t distance = scores.size() / 2;
    for (int64_t i = 0; i < distance; i++)
    {
        scores.pop();
    }
    std::cout << "score was: " << scores.top() << std::endl;
}