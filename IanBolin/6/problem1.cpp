#include <vector>
#include <iostream>

int main()
{
    std::vector<int64_t> fishes = {1, 2, 1, 3, 2, 1, 1, 5, 1, 4, 1, 2, 1, 4, 3, 3, 5, 1, 1, 3, 5, 3, 4, 5, 5, 4, 3, 1, 1, 4, 3, 1, 5, 2, 5, 2, 4, 1, 1, 1, 1, 1, 1, 1, 4, 1, 4, 4, 4, 1, 4, 4, 1, 4, 2, 1, 1, 1, 1, 3, 5, 4, 3, 3, 5, 4, 1, 3, 1, 1, 2, 1, 1, 1, 4, 1, 2, 5, 2, 3, 1, 1, 1, 2, 1, 5, 1, 1, 1, 4, 4, 4, 1, 5, 1, 2, 3, 2, 2, 2, 1, 1, 4, 3, 1, 4, 4, 2, 1, 1, 5, 1, 1, 1, 3, 1, 2, 1, 1, 1, 1, 4, 5, 5, 2, 3, 4, 2, 1, 1, 1, 2, 1, 1, 5, 5, 3, 5, 4, 3, 1, 3, 1, 1, 5, 1, 1, 4, 2, 1, 3, 1, 1, 4, 3, 1, 5, 1, 1, 3, 4, 2, 2, 1, 1, 2, 1, 1, 2, 1, 3, 2, 3, 1, 4, 5, 1, 1, 4, 3, 3, 1, 1, 2, 2, 1, 5, 2, 1, 3, 4, 5, 4, 5, 5, 4, 3, 1, 5, 1, 1, 1, 4, 4, 3, 2, 5, 2, 1, 4, 3, 5, 1, 3, 5, 1, 3, 3, 1, 1, 1, 2, 5, 3, 1, 1, 3, 1, 1, 1, 2, 1, 5, 1, 5, 1, 3, 1, 1, 5, 4, 3, 3, 2, 2, 1, 1, 3, 4, 1, 1, 1, 1, 4, 1, 3, 1, 5, 1, 1, 3, 1, 1, 1, 1, 2, 2, 4, 4, 4, 1, 2, 5, 5, 2, 2, 4, 1, 1, 4, 2, 1, 1, 5, 1, 5, 3, 5, 4, 5, 3, 1, 1, 1, 2, 3, 1, 2, 1, 1};
    // std::vector<int64_t> fishes = {3, 4, 3, 1, 2};

    const int64_t num_days = 80;
    // const int64_t num_days = 18
    for (int64_t i = 0; i < num_days; i++)
    {
        std::vector<int64_t> new_fishes;
        for (int64_t &fish : fishes)
        {
            fish--;
            if (fish == -1)
            {
                new_fishes.emplace_back(8);
                fish = 6;
            }
        }
        fishes.insert(fishes.end(), std::make_move_iterator(new_fishes.begin()), std::make_move_iterator(new_fishes.end()));
    }
    std::cout << "On day " << num_days << " there are " << fishes.size() << " fish" << std::endl;

    return 0;
}