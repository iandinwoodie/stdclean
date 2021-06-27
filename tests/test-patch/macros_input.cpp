#include "macros.hpp"

#ifdef _WIN32
#include <windows.h>
auto s = wstring;
#else
auto s = string;
#endif

auto s = u8string;
