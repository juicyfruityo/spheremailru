#include<iostream>
#include<vector>
#include<stdexcept>


class Matrix {
 public:
   Matrix(int rows, int cols)
          : rows(rows), cols(cols) {
     matr.reserve(rows);
     for (int i=0; i<rows; ++i) {
        matr[i].reserve(cols);
     }
   }



   class Array {
    public:
      Array(int cols, std::vector<int>& v):
            cols(cols)
            {
              vec.reserve(cols);
              for (int i=0; i<cols; ++i) {
                  vec[i] = v[i];
              }
            }
      int& operator[](int c) {
          if (c >= cols) throw std::out_of_range("");
          return vec[c];
      }
    private:
      const int cols;
      std::vector<int> vec;
   };

   Array operator[](int r) {
      if (r >= rows) throw std::out_of_range("");
      return Array(cols, matr[r]);
   }



   int getRows() {
      return rows;
   }

   int getColumns() {
      return cols;
   }

   void getNumbers() {
      for (int i=0; i<rows; ++i) {
          for (int j=0; j<cols; ++j) {
              matr[i][j] = i + j;
          }
      }
   }

 //private:
   const int rows;
   const int cols;
   std::vector<std::vector<int> > matr;
};


int main() {
    Matrix m(5, 3);
    m.getNumbers();
    //m[1][1] = 3;

    //std::cout << m.matr[3][2] << '\n';
    m[4][2] = 15;
    std::cout << m[4][2] << '\n';
    return 0;
}
