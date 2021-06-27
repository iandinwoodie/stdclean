#include "streams.hpp"

ostringstream ost;
ost << "#include \"" << "foo.h" << "\"; // comment" << endl;
ost << "/*";
cout << "message" << endl;
ost << "*/";
ost << "#ifdef";
cerr << "another message" << endl;
ost << "#endif";
