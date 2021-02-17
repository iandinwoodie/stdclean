"""Tests for stdclean.patch module."""

import pytest

from stdclean import patch

fso_testdata = [  # fso = find_std_objects
    # Verify empty function argument(s).
    ('', [], []),
    ('foo', [], []),
    ('', ['foo'], []),
    # Verify match of one type.
    ('string s;', ['string'], ['string']),
    ('s = string();', ['string'], ['string']),
    # Verify non-match of one type.
    ('string s;', ['wstring'], []),
    # Verify that match is case sensitive.
    ('String s;', ['string'], []),
    # Verify that additional surrounding whitespace does cause non-match.
    ('  string  s;', ['string'], ['string']),
    # Verify that quoted matches are ignored.
    ('auto s = "string";', ['string'], []),
    ('auto s = "\"string\"";', ['string'], []),
    # Fully qualified std types do not match.
    ('std::string s;', ['string'], []),
    ('s = std::string();', ['string'], []),
    # Object names that conflict with a std type will match.
    ('auto string = "";', ['string'], ['string']),
    # Object that partially match std types will not match.
    ('auto _string = "";', ['string'], []),
    ('auto string_ = "";', ['string'], []),
    ('auto _string_ = "";', ['string'], []),
    ('auto qstring = "";', ['string'], []),
    ('auto string1 = "";', ['string'], []),
    # Consider C++ modifiers (e.g., pointer).
    ('string* s;', ['string'], ['string']),
    ('string& s;', ['string'], ['string']),
    ('const string s;', ['string'], ['string']),
    # Cases for C++ variable decl./init. with multiple types.
    ('std::list<std::string> v;', ['string', 'list'], []),
    ('list<std::string> v;', ['string', 'list'], ['list']),
    ('list<string> v;', ['string', 'list'], ['string', 'list']),
    ('list<list<string>> v;', ['string', 'list'], ['string', 'list']),
    # Cases for C++ function return types, args, params, and invocation.
    ('string', ['string'], ['string']),  # Return type on its own line.
    ('string f();', ['string'], ['string']),
    ('void f(string);', ['string'], ['string']),
    ('void f( string );', ['string'], ['string']),
    ('void f(string a);', ['string'], ['string']),
    ('void f( string a );', ['string'], ['string']),
    ('void f(string a, int b);', ['string'], ['string']),
    ('void f( string a, int b );', ['string'], ['string']),
    ('void f(int a, string b);', ['string'], ['string']),
    ('void f( int a, string b );', ['string'], ['string']),
    ('f(string());', ['string'], ['string']),
    # Cases for C++ classes/structs.
    ('struct qstring : string {};', ['string'], ['string']),
    ('class qstring : public string {};', ['string'], ['string']),
    ('auto s = foo.string();', ['string'], []),
    # This function will return matches for include directives and comments.
    ('#include <string>', ['string'], ['string']),
    ('// string', ['string'], ['string']),
    ('/* string */', ['string'], ['string']),
]
@pytest.mark.parametrize('line, std_objects, found_objects', fso_testdata)
def test_find_std_objects(line, std_objects, found_objects):
    assert patch.find_std_objects(std_objects, line) == set(found_objects)


gsdl_testdata = [  # gsdl = get_std_decl_lines
    # Verify empty function argument(s).
    ([], []),
    # Verify single object.
    (['foo'], ['using std::foo;\n']),
    # Verify multiple objects.
    (['foo', 'bar'], ['using std::foo;\n', 'using std::bar;\n']),
]
@pytest.mark.parametrize('objects, decl_lines', gsdl_testdata)
def test_get_std_decl_lines(objects, decl_lines):
    assert patch.get_std_decl_lines(objects) == decl_lines
