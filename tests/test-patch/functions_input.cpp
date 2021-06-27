#include "functions.hpp"

string f(wstring);
std::u8string f(std::u16string);
list<u32string> f(void);
void f(vector<stringbuf>);
auto s = f(multiset());
// Below will result in false positives.
void swap(void);
void hash(void);
