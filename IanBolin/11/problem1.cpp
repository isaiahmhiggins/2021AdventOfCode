#include <iostream>
#include <vector>

void update_cell(int64_t row, int64_t col, std::vector<std::vector<int64_t>> &map, std::vector<std::vector<bool>> &flash_map);

bool valid_location(int64_t row, int64_t col)
{
    return (row < 10 && row >= 0 && col < 10 && col >= 0);
}

void update_neighbors(int64_t row, int64_t col, std::vector<std::vector<int64_t>> &map, std::vector<std::vector<bool>> &flash_map)
{
    for (int64_t target_row = row - 1; target_row <= row + 1; target_row++)
    {
        for (int64_t target_col = col - 1; target_col <= col + 1; target_col++)
        {
            if (target_row == row && target_col == col)
            {
                continue;
            }
            if (valid_location(target_row, target_col))
            {
                update_cell(target_row, target_col, map, flash_map);
            }
        }
    }
}
void update_cell(int64_t row, int64_t col, std::vector<std::vector<int64_t>> &map, std::vector<std::vector<bool>> &flash_map)
{
    map.at(row).at(col)++;
    int64_t val = map.at(row).at(col);
    if (val > 9 && !flash_map.at(row).at(col))
    {
        flash_map.at(row).at(col) = true;
        update_neighbors(row, col, map, flash_map);
    }
}

int main()
{
    std::vector<std::vector<int64_t>> map = {{7, 7, 7, 7, 8, 3, 8, 3, 5, 3},
                                             {2, 2, 1, 7, 2, 7, 2, 4, 7, 8},
                                             {3, 3, 5, 5, 3, 1, 8, 6, 4, 5},
                                             {2, 2, 4, 2, 6, 1, 8, 1, 1, 3},
                                             {7, 1, 8, 2, 4, 6, 8, 6, 6, 6},
                                             {5, 4, 4, 1, 6, 4, 1, 1, 1, 1},
                                             {4, 7, 7, 3, 8, 6, 2, 3, 6, 4},
                                             {5, 7, 1, 7, 1, 2, 5, 5, 2, 1},
                                             {7, 5, 4, 2, 1, 2, 7, 7, 2, 1},
                                             {4, 5, 7, 6, 6, 7, 8, 3, 4, 1}};

    // test data
    // std::vector<std::vector<int64_t>> map = {{7, 7, 7, 7, 8, 3, 8, 3, 5, 3},
    //                                          {2, 2, 1, 7, 2, 7, 2, 4, 7, 8},
    //                                          {3, 3, 5, 5, 3, 1, 8, 6, 4, 5},
    //                                          {2, 2, 4, 2, 6, 1, 8, 1, 1, 3},
    //                                          {7, 1, 8, 2, 4, 6, 8, 6, 6, 6},
    //                                          {5, 4, 4, 1, 6, 4, 1, 1, 1, 1},
    //                                          {4, 7, 7, 3, 8, 6, 2, 3, 6, 4},
    //                                          {5, 7, 1, 7, 1, 2, 5, 5, 2, 1},
    //                                          {7, 5, 4, 2, 1, 2, 7, 7, 2, 1},
    //                                          {4, 5, 7, 6, 6, 7, 8, 3, 4, 1}};

    std::vector<std::vector<bool>> flash_map = {{false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false},
                                                {false, false, false, false, false, false, false, false, false, false}};

    int64_t flashes = 0;
    for (int64_t day = 0; day < 100; day++)
    {
        for (int64_t row = 0; row < 10; row++)
        {
            for (int64_t col = 0; col < 10; col++)
            {
                update_cell(row, col, map, flash_map);
            }
        }
        for (int64_t row = 0; row < 10; row++)
        {
            for (int64_t col = 0; col < 10; col++)
            {
                if (flash_map.at(row).at(col))
                {
                    flashes++;
                    map.at(row).at(col) = 0;
                }
                flash_map.at(row).at(col) = false;
            }
        }
    }

    std::cout << "flashes: " << flashes << std::endl;

    return 0;
}