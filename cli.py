#!/usr/bin/python

from sys import argv
from typing import List

from numpy import array
from numpy.typing import NDArray
from src.list_parser import parse
from src.demidovich import run_demidovich
from src.kostrikin import run_kostrikin
from src.task2 import solve_system_of_linear_equations_numerically


def print_help() -> None:
    print('''
usage: cli.py [options] [arguments]
            
Options:
    --demidovich        print solitions for problems from demidovich problem set,
                        graphs are saved to ./graphs
    
    --kostrikin         print solutions for problems from kostrikin problem set 
    
    --task2 <A> <B>     solve system Ax=B for provided A and B, A and B are
                        given in form of space separeted values, inside nested 
                        brackets (any of <>, (), [], {}); 
                        Example usage : cli.py --task2 [[1, 2], [3, 4]] (5, 6)  
    
    --help              see this help

            ''')

def convert_input_to_array(input: str) -> NDArray:
    try:
        return array(parse(input))
    except ValueError:
        raise ValueError("Inputed list has incorrect dimensions")


def run_task2(a: str, b: str):
    return solve_system_of_linear_equations_numerically(
        convert_input_to_array(a), convert_input_to_array(b))


def parse_args(input: List[str]):
    match input:
        case [_, '--help', *_]:
            print_help()
        case [_, '--demidovich', *_]:
            run_demidovich()
        case [_, '--kostrikin', *_]:
            run_kostrikin()
        case [_, '--task2', a, b, *_]:
            run_task2(a, b)
        case _:
            print("Invalid options")
            print_help()


def main() -> None:
    parse_args(argv)


if __name__ == "__main__":
    main()
