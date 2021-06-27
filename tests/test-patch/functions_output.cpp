#include "functions.hpp"
using std::hash;
using std::list;
using std::multiset;
using std::string;
using std::stringbuf;
using std::swap;
using std::u32string;
using std::vector;
using std::wstring;

string f(wstring);
std::u8string f(std::u16string);
list<u32string> f(void);
void f(vector<stringbuf>);
auto s = f(multiset());
// Below are false positives
void swap(void);
void hash(void);
