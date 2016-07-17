#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Similar to C++ parser made in Python"""
from __future__ import print_function
import argparse
import sys, traceback
import lexer_rules
import parser_rules
from sys import argv, exit
import lex
import yacc

def parseInput() :
    parser = argparse.ArgumentParser(
        description='A C++ basic parser',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,# ArgumentDefaultsHelpFormatter
        epilog='''Authors: Cyntia Bonomi, Alan Castro and Sabrina Izcovich''')
    parser.add_argument('-o', type=argparse.FileType('w'), nargs='?',  default=sys.stdout, help='outputFilename')
    parser.add_argument('-c', type=argparse.FileType('r'), nargs='?', default=sys.stdin, help='inputFilename')
    args = parser.parse_args()
    if not parser.parse_args(['-o', '-c']):
        print("The program should be called as ./SLSParser [-o EXIT] [-c ENTRY | SOURCE]", file=sys.stderr)
    return args

def dump_ast(ast, output_file):
    output_file.write("digraph {\n")
    key = frozenset(ast.items())
    edges = []
    queue = [ast]
    numbers = {ast: 1}
    current_number = 2
    while len(queue) > 0:
        node = queue.pop(0)
        name = node.name()
        number = numbers[node]
        output_file.write('node[width=1.5, height=1.5, shape="circle", label="%s"] n%d;\n' % (name, number))
        for child in node.children():
            numbers[child] = current_number
            edge = 'n%d -> n%d;\n' % (number, current_number)
            edges.append(edge)
            queue.append(child)
            current_number += 1
    output_file.write("".join(edges))
    output_file.write("}")


if __name__ == "__main__":
    try:
        args = parseInput()
        text = args.c.read()
        lexer = lex.lex(module=lexer_rules)
        parser = yacc.yacc(module=parser_rules)
        ast = parser.parse(text, lexer)
        print(ast["value"],file = args.o)
    except:
        sys.exit(1)
        raise Exception("The syntax is not valid.")
