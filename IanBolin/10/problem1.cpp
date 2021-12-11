#include <iostream>
#include <fstream>
#include <stack>

int64_t score_char(char c)
{
    int64_t val = 0;
    if (c == ')')
    {
        val = 3;
    }
    else if (c == ']')
    {
        val = 57;
    }
    else if (c == '}')
    {
        val = 1197;
    }
    else if (c == '>')
    {
        val = 25137;
    }

    return val;
}

int main()
{
    std::ifstream input("input.txt");
    int64_t score = 0;
    while (!input.eof())
    {
        std::string line;
        input >> line;
        std::stack<char> opening;
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
                    score += score_char(loc);
                    break;
                }
                else if (last_open == '[' && loc != ']')
                {
                    score += score_char(loc);
                    break;
                }
                else if (last_open == '{' && loc != '}')
                {
                    score += score_char(loc);
                    break;
                }
                else if (last_open == '<' && loc != '>')
                {
                    score += score_char(loc);
                    break;
                }
            }
        }
    }
    std::cout << "score was: " << score << std::endl;
}