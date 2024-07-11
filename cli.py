#!/usr/bin/python

from sys import argv
from typing import List

from numpy.typing import NDArray
from src.parser import parse, validate_parsed
from src.demidovich import run_demidovich
from src.kostrikin import run_kostrikin
from src.task2 import solve_system_of_linear_equations_numerically


def get_help() -> str:
    return '''
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

            '''


def run_task2(a: str, b: str):
    A = parse(a)
    B = parse(b)
    if isinstance(a, float):
        A = [A]
    if isinstance(b, float):
        B = [B]
    A = validate_parsed(A)  # type: ignore
    B = validate_parsed(B)  # type: ignore
    return solve_system_of_linear_equations_numerically(A, B)


def parse_args(input: List[str]):
    match input:
        case [_, '--help']:
            print(get_help())
        case [_, '--demidovich']:
            run_demidovich()
        case [_, '--kostrikin']:
            run_kostrikin()
        case [_, '--task2', a, b]:
            run_task2(a, b)
        case _:
            print("Invalid options")
            print(get_help())


def main() -> None:
    parse_args(argv)
    # pass


if __name__ == "__main__":
    # print(argv)
    main()
