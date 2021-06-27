#include "streams.hpp"
using std::cerr;
using std::cout;
using std::endl;
using std::ostringstream;

ostringstream ost;
ost << "#include \"" << "foo.h" << "\"; // comment" << endl;
ost << "/*";
cout << "message" << endl;
cerr << "another message" << endl;
ost << "*/";
