#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Create Date: 2018-10-19 10:40
# Author: Airlam

# Instruction opcodes for compiled code


opname = [
"STOP_CODE",	# 0
"POP_TOP",		# 1
"ROT_TWO",		# 2
"ROT_THREE",	# 3
"DUP_TOP",		# 4
"ROT_FOUR",	    # 5
"__6",          # 6
"__7",          # 7
"__8",          # 8
"NOP",		    # 9
"UNARY_POSITIVE",	# 10
"UNARY_NEGATIVE",	# 11
"UNARY_NOT",	    # 12
"UNARY_CONVERT",	# 13
"__14",             # 14
"UNARY_INVERT",	    # 15
"__16",             # 16
"__17",             # 17
"LIST_APPEND",	    # 18
"BINARY_POWER",	    # 19
"BINARY_MULTIPLY",	# 20
"BINARY_DIVIDE",	# 21
"BINARY_MODULO",	# 22
"BINARY_ADD",	    # 23
"BINARY_SUBTRACT",	# 24
"BINARY_SUBSCR",	# 25
"BINARY_FLOOR_DIVIDE", # 26
"BINARY_TRUE_DIVIDE", # 27
"INPLACE_FLOOR_DIVIDE", # 28
"INPLACE_TRUE_DIVIDE", # 29
"SLICE",		    # 30 /* Also uses 31-33 */
"__31",             # 31
"__32",             # 32
"__33",             # 33
"__34",             # 34
"__35",             # 35
"__36",             # 36
"__37",             # 37
"__38",             # 38
"__39",             # 39
"STORE_SLICE",	    # 40 /* Also uses 41-43 */
"_",                # 41
"_",                # 42
"_",                # 43
"_",                # 44
"_",                # 45
"_",                # 46
"_",                # 47
"_",                # 48
"_",                # 49
"DELETE_SLICE", 	# 50 /* Also uses 51-53 */
"_",                # 51
"_",                # 52
"_",                # 53
"_",                # 54
"INPLACE_ADD",	    # 55
"INPLACE_SUBTRACT",	# 56
"INPLACE_MULTIPLY",	# 57
"INPLACE_DIVIDE",	# 58
"INPLACE_MODULO",	# 59
"STORE_SUBSCR", 	# 60
"DELETE_SUBSCR",	# 61 
"BINARY_LSHIFT",	# 62
"BINARY_RSHIFT",	# 63
"BINARY_AND",	    # 64
"BINARY_XOR",	    # 65
"BINARY_OR",	    # 66
"INPLACE_POWER",	# 67
"GET_ITER",	        # 68 
"_",                # 69
"PRINT_EXPR",	    # 70
"PRINT_ITEM",	    # 71
"PRINT_NEWLINE",	# 72
"PRINT_ITEM_TO",    # 73
"PRINT_NEWLINE_TO", # 74
"INPLACE_LSHIFT",	# 75
"INPLACE_RSHIFT",	# 76
"INPLACE_AND",	    # 77
"INPLACE_XOR",	    # 78
"INPLACE_OR",	    # 79
"BREAK_LOOP",	    # 80
"WITH_CLEANUP",     # 81
"LOAD_LOCALS",	    # 82
"RETURN_VALUE",	    # 83
"IMPORT_STAR",	    # 84
"EXEC_STMT",	    # 85
"YIELD_VALUE",	    # 86
"POP_BLOCK",	    # 87
"END_FINALLY",	    # 88
"BUILD_CLASS",	    # 89 
"STORE_NAME",	    # 90	# "HAVE_ARGUMENT": Opcodes from here have an argument;  Index in name list
"DELETE_NAME",	    # 91	/* "" */
"UNPACK_SEQUENCE",	# 92	/* Number of sequence items */
"FOR_ITER",	        # 93 
"_",                # 94
"STORE_ATTR",	    # 95	/* Index in name list */
"DELETE_ATTR",	    # 96	/* "" */
"STORE_GLOBAL",	    # 97	/* "" */
"DELETE_GLOBAL",	# 98	/* "" */
"DUP_TOPX",	        # 99	/* number of items to duplicate */
"LOAD_CONST",	    # 100	/* Index in const list */
"LOAD_NAME",	    # 101	/* Index in name list */
"BUILD_TUPLE",	    # 102	/* Number of tuple items */
"BUILD_LIST",	    # 103	/* Number of list items */
"BUILD_MAP",	    # 104	/* Always zero for now */
"LOAD_ATTR",	    # 105	/* Index in name list */
"COMPARE_OP",	    # 106	/* Comparison operator */
"IMPORT_NAME",	    # 107	/* Index in name list */
"IMPORT_FROM",	    # 108	/* Index in name list */ 
"_109",             # 109
"JUMP_FORWARD",	    # 110	/* Number of bytes to skip */
"JUMP_IF_FALSE",	# 111	/* "" */
"JUMP_IF_TRUE",	    # 112	/* "" */
"JUMP_ABSOLUTE",	# 113	/* Target byte offset from beginning of code */ 
"_114",             # 114
"_115",             # 115
"LOAD_GLOBAL",	    # 116	/* Index in name list */ 
"_117",             # 117
"_118",             # 118
"CONTINUE_LOOP",	# 119	/* Start of loop (absolute) */
"SETUP_LOOP",	    # 120	/* Target address (absolute) */
"SETUP_EXCEPT",	    # 121	/* "" */
"SETUP_FINALLY",	# 122	/* "" */ 
"_123",             # 123
"LOAD_FAST",	    # 124	/* Local variable number */
"STORE_FAST",	    # 125	/* Local variable number */
"DELETE_FAST",	    # 126	/* Local variable number */ 
"_127",             # 127
"_128",             # 128
"_129",             # 129
"RAISE_VARARGS",	# 130	/* Number of raise arguments (1, 2 or 3) */ /* CALL_FUNCTION_XXX opcodes defined below depend on this definition */
"CALL_FUNCTION",	# 131	/* #args + (#kwargs<<8) */
"MAKE_FUNCTION",	# 132	/* #defaults */
"BUILD_SLICE", 	    # 133	/* Number of items */ 
"MAKE_CLOSURE",     # 134     /* #free vars */
"LOAD_CLOSURE",     # 135     /* Load free variable from closure */
"LOAD_DEREF",       # 136     /* Load and dereference from closure cell */ 
"STORE_DEREF",      # 137     /* Store into cell */ /* The next 3 opcodes must be contiguous and satisfy (CALL_FUNCTION_VAR - CALL_FUNCTION) & 3 == 1  */
"_138",             # 138
"_139",             # 139
"CALL_FUNCTION_VAR",          # 140	/* #args + (#kwargs<<8) */
"CALL_FUNCTION_KW",           # 141	/* #args + (#kwargs<<8) */
"CALL_FUNCTION_VAR_KW",       # 142	/* #args + (#kwargs<<8) */ /* Support for opargs more than 16 bits long */
"EXTENDED_ARG",               # 143
]

HAVE_ARGUMENT = 90  # Opcodes from here have an argument

def HAS_ARG(op):
    return op >= HAVE_ARGUMENT

