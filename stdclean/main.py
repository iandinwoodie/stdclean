"""Main entry point for the stdclean command."""

from stdclean.find import find_cpp_file_paths
from stdclean.patch import patch_with_std_decl

STD_LIB_DEFAULT_MAPPING = {
    'bitset': [
        'bitset',
    ],
    'csetjmp': [
        'jmp_buf',
        'setjmp',
        'longjmp'
    ]
    'csignal': [
        'sig_atomic_t',
        'signal',
        'raise',
    ],
    'cstdarg': [
        'va_list',
        'va_start',
        'va_copy',
        'va_end',
    ],
    'cstdlib': [
        'div_t',
        'ldiv_t',
        'lldiv_t',
        'size_t',
        'abort',
        'exit',
        'quick_exit',
        '_Exit',
        'atexit',
        'at_quick_exit',
        'system',
        'getenv',
        'malloc',
        'aligned_alloc',
        'calloc',
        'realloc',
        'free',
        'atof',
        'atoi',
        'atol',
        'atoll',
        'strtol',
        'strtoll',
        'strtoul',
        'strtoull',
        'strtof',
        'strtod',
        'strtold',
        'mblen',
        'mbtowc',
        'wctomb',
        'mbstowcs',
        'wcstombs',
        'rand',
        'srand',
        'qsort',
        'bsearch',
        'abs',
        'labs',
        'llabs',
        'div',
        'ldiv',
        'lldiv',
    ]
    'string': [
        'basic_string',
        'string',
        'u8string',
        'u16string',
        'u32string',
        'wstring',
    ],
    'vector': [
        'vector',
    ]
}


def stdclean(target):
    path_list = find_cpp_file_paths(target)
    for path in path_list:
        print(path)
        patch_with_std_decl(path, STD_LIB_DEFAULT_MAPPING)
