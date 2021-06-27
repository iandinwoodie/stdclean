#include "macros.hpp"
using std::string;
using std::u16string;
using std::u32string;

#ifdef _WIN32
#include <windows.h>
auto s = u32string;
#else
auto s = u16string;
#endif

auto s = string;
