"""Main entry point for the stdclean command."""

from stdclean.find import find_cpp_file_paths
from stdclean.patch import patch_with_std_decl

STD_LIB_DEFAULT_MAPPING = {
    'any': [
        'any',
        'bad_any_cast',
        'swap',
        'make_any',
        'any_cast',
    ],
    'array': [
        # incomplete
        'array',
    ],
    'bitset': [
        'bitset',
        'hash',
    ],
    'csetjmp': [
        'jmp_buf',
        'setjmp',
        'longjmp'
    ],
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
    'cstddef': [
        'size_t',
        'ptrdiff_t',
        'nullptr_t',
        'max_allign_t',
        'byte'
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
    ],
    'deque': [
        # incomplete
        'deque',
    ],
    'forward_list': [
        # incomplete
        'forward_list',
    ],
    'functional': [
        'placeholders',
        'function',
        'mem_fn',
        'bad_function_call',
        'is_bind_expression',
        'is_placeholder',
        'reference_wrapper',
        'hash',
    ],
    'limits': [
        'numeric_limits',
        'float_round_style',
        'float_denorm_style',
    ],
    'list': [
        # incomplete
        'list',
    ],
    'map': [
        # incomplete
        'map',
    ],
    'new': [
        'bad_alloc',
        'bad_array_new_length',
        'nothrow_t',
        'align_val_t',
        'destroying_delete_t',
        'new_handler',
        'no_throw',
        'hardware_destructive_interference_size',
        'hardware_constructive_interference_size',
    ],
    'optional': [
        'optional',
        'bad_optional_access',
        'hash',
        'nullopt',
        'swap',
        'make_optional',
    ],
    'set': [
        # incomplete
        'set',
    ],
    'span': [
        # incomplete
        'span',
    ],
    'stack': [
        # incomplete
        'stack',
    ],
    'string': [
        # incomplete
        'basic_string',
        'string',
        'u8string',
        'u16string',
        'u32string',
        'wstring',
    ],
    'type_traits': [
        'integral_constant',
        'bool_constant',
        'true_type',
        'false_type',
        'is_void',
        'is_null_pointer',
        'is_integral',
        'is_floating_point',
        'is_array',
        'is_pointer',
        'is_lvalue_reference',
        'is_rvalue_reference',
        'is_member_object_pointer',
        'is_member_function_pointer',
        'is_enum',
        'is_union',
        'is_class',
        'is_function',
        'is_reference',
        'is_arithmetic',
        'is_fundamental',
        'is_object',
        'is_scalar',
        'is_compound',
        'is_member_pointer',
        'is_const',
        'is_volatile',
        'is_trivial',
        'is_trivially_copyable',
        'is_standard_layout',
        'is_pod',
        'is_empty',
        'is_polymorphic',
        'is_abstract',
        'is_final',
        'is_aggregate',
        'is_signed',
        'is_unsigned',
        'is_bounded_array',
        'is_unbounded_array',
        'is_scoped_enum',
        'is_constructible',
        'is_default_constructible',
        'is_copy_constructible',
        'is_move_constructible',
        'is_assignable',
        'is_copy_assignable',
        'is_move_assignable',
        'is_swappable_with',
        'is_swappable',
        'is_destructible',
        'is_trivially_constructible',
        'is_trivially_default_constructible',
        'is_trivially_copy_constructible',
        'is_trivially_move_constructible',
        'is_trivially_assignable',
        'is_trivially_copy_assignable',
        'is_trivially_move_assignable',
        'is_trivially_destructible',
        'is_nothrow_constructible',
        'is_nothrow_default_constructible',
        'is_nothrow_copy_constructible',
        'is_nothrow_move_constructible',
        'is_nothrow_assignable',
        'is_nothrow_copy_assignable',
        'is_nothrow_move_assignable',
        'is_nothrow_swappable_with',
        'is_nothrow_swappable',
        'is_nothrow_destructible',
        'has_virtual_destructor',
        'has_unique_object_representations',
        'alignment_of',
        'rank',
        'extent',
        'is_same',
        'is_base_of',
        'is_convertible',
        'is_nothrow_convertible',
        'is_layout_compatible',
        'is_pointer_interconvertible_base_of',
        'is_invocable',
        'is_invocable_r',
        'is_nothrow_invocable',
        'is_nothrow_invocable_r',
        'remove_const',
        'remove_volatile',
        'remove_cv',
        'add_const',
        'add_volatile',
        'add_cv',
        'remove_const_t',
        'remove_volatile_t',
        'remove_cv_t',
        'add_const_t',
        'add_volatile_t',
        'add_cv_t',
        'remove_reference',
        'add_lvalue_reference',
        'add_rvalue_reference',
        'remove_reference_t',
        'add_lvalue_reference_t',
        'add_rvalue_reference_t',
        'make_signed',
        'make_unsigned',
        'make_signed_t',
        'make_unsigned_t',
        'remove_extent',
        'remove_all_extents',
        'remove_extent_t',
        'remove_all_extents_t',
        'remove_pointer',
        'add_pointer',
        'remove_pointer_t',
        'add_pointer_t',
        'aligned_storage',
        'aligned_union',
        'decay',
        'remove_cvref',
        'enable_if',
        'conditional',
        'common_type',
        'underlying_type',
        'result_of',
        'invoke_result',
        'aligned_storage_t',
        'aligned_union_t',
        'decay_t',
        'remove_cvref_t',
        'enable_if_t',
        'conditional_t',
        'common_type_t',
        'underlying_type_t',
        'result_of_t',
        'invoke_result_t',
        'void_t',
        'conjunction',
        'disjunction',
        'negation',
        'is_void_v',
        'is_null_pointer_v',
        'is_integral_v',
        'is_floating_point_v',
        'is_array_v',
        'is_pointer_v',
        'is_lvalue_reference_v',
        'is_rvalue_reference_v',
        'is_member_object_pointer_v',
        'is_member_function_pointer_v',
        'is_enum_v',
        'is_union_v',
        'is_class_v',
        'is_function_v',
        'is_reference_v',
        'is_arithmetic_v',
        'is_fundamental_v',
        'is_object_v',
        'is_scalar_v',
        'is_compound_v',
        'is_member_pointer_v',
        'is_const_v',
        'is_volatile_v',
        'is_trivial_v',
        'is_trivially_copyable_v',
        'is_standard_layout_v',
        'is_pod_v',
        'is_empty_v',
        'is_polymorphic_v',
        'is_abstract_v',
        'is_final_v',
        'is_aggregate_v',
        'is_signed_v',
        'is_unsigned_v',
        'is_bounded_array_v',
        'is_unbounded_array_v',
        'is_scoped_enum_v',
        'is_constructible_v',
        'is_default_constructible_v',
        'is_copy_constructible_v',
        'is_move_constructible_v',
        'is_assignable_v',
        'is_copy_assignable_v',
        'is_move_assignable_v',
        'is_swappable_with_v',
        'is_swappable_v',
        'is_destructible_v',
        'is_trivially_constructible_v',
        'is_trivially_default_constructible_v',
        'is_trivially_copy_constructible_v',
        'is_trivially_move_constructible_v',
        'is_trivially_assignable_v',
        'is_trivially_copy_assignable_v',
        'is_trivially_move_assignable_v',
        'is_trivially_destructible_v',
        'is_nothrow_constructible_v',
        'is_nothrow_default_constructible_v',
        'is_nothrow_copy_constructible_v',
        'is_nothrow_move_constructible_v',
        'is_nothrow_assignable_v',
        'is_nothrow_copy_assignable_v',
        'is_nothrow_move_assignable_v',
        'is_nothrow_swappable_with_v',
        'is_nothrow_swappable_v',
        'is_nothrow_destructible_v',
        'has_virtual_destructor_v',
        'has_unique_object_representations_v',
        'alignment_of_v',
        'rank_v',
        'extent_v',
        'is_same_v',
        'is_base_of_v',
        'is_convertible_v',
        'is_nothrow_convertible_v',
        'is_layout_compatible_v',
        'is_pointer_interconvertible_base_of_v',
        'is_invocable_v',
        'is_invocable_r_v',
        'is_nothrow_invocable_v',
        'is_nothrow_invocable_r_v',
        'conjunction_v',
        'disjunction_v',
        'negation_v',
        'is_pointer_interconvertible_with_class',
        'is_corresponding_member',
        'is_constant_evaluated',
    ],
    'typeinfo': [
        'type_info',
        'bad_cast',
        'bad_typeid',
    ],
    'unordered_map': [
        # incomplete
        'unordered_map',
    ],
    'unordered_set': [
        # incomplete
        'unordered_set',
    ],
    'utility': [
        'rel_ops',
        'swap',
        'exchange',
        'forward',
        'move',
        'move_if_noexcept',
        'as_const',
        'declval',
        'cmp_equal',
        'cmp_not_equal',
        'cmp_less',
        'cmp_greater',
        'cmp_less_equal',
        'cmp_greater_equal',
        'in_range',
        'make_pair',
        'get',
        'pair',
        'integer_sequence',
        'tuple',
        'piecewise_construct_t',
        'piecewise_construct',
        'in_place',
        'in_place_type',
        'in_place_index',
        'in_place_t',
        'in_place_type_t',
        'in_place_index_t',
    ],
    'vector': [
        # incomplete
        'vector',
    ]
}


def stdclean(target):
    path_list = find_cpp_file_paths(target)
    for path in path_list:
        with open(path, 'r') as fp:
            lines = fp.readlines()
        lines = patch_with_std_decl(lines, STD_LIB_DEFAULT_MAPPING)
        if lines:
            with open(path, 'w') as fp:
                fp.writelines(lines)
            print('patched: {}'.format(path))
