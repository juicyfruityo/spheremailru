#include <iostream>
#include <vector>
#include <cmath>
#include "numbers.dat"


int BinSearch(size_t, size_t, int);
bool IsSimple(const int);


bool IsSimple(const int x) {
    for (int i = 2; i <= sqrt(x); ++i) {
        if (x % i == 0) {
            return false;
        }
    }
    if (x == 1)   return false;
    return true;
}


int BinSearch(size_t begin, size_t end, int value) {
    size_t middle = (end + begin) / 2;

    if (Data[middle] == value) {
      int index = middle;
      while (Data[index - 1] == value) {
          index--;
      }
      return index;
    } else if (middle == end || middle == begin) {
        return -1;
    } else if (Data[middle] > value) {
        return BinSearch(begin, middle, value);
    } else if (Data[middle] < value) {
        return BinSearch(middle, end, value);
    }
}


int main(int argc, char* argv[]) {
  std::vector<std::pair<int, int> > arg;

  if (argc == 1) {
      return -1;
  }
  for (size_t i = 1; i < argc; ++i) {
        int x = std::atoi(argv[i]);
        i++;
        if (i >= argc) {
            return -1;
        }
        int y = std::atoi(argv[i]);
        arg.push_back(std::make_pair(x, y));
    }

  for (size_t i = 0; i < arg.size(); ++i) {
      int ind0 = BinSearch(0, Size, arg[i].first);
      int ind1 = BinSearch(0, Size, arg[i].second);
      if (ind0 == -1 || ind1 == -1) {
          return -1;
      }

      int count = 0;
      for (size_t j = ind0; j <= ind1; ++j) {
          if (IsSimple(Data[j]))    count++;
      }
      std::cout << count << std::endl;
  }

  return 0;
}
