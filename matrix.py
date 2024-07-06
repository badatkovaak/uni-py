from collections.abc import Sequence
from types import FunctionType
from typing import Callable, Iterator, List, Optional
import numpy as np
from numpy.typing import NDArray
from dataclasses import dataclass


@dataclass(slots=True)
class Peekable[T]:
    data: Sequence[T]
    position: int = -1

    def peek(self) -> Optional[T]:
        if self.position + 1 < len(self.data):
            return self.data[self.position + 1]
        return None

    def __next__(self) -> T:
        if self.position >= len(self.data):
            raise StopIteration
        self.position += 1
        return self.data[self.position - 1]

    def __iter__(self) -> Iterator[T]:
        return self


def parse_number(input: Peekable[str]) -> float:
    next_char = input.peek()
    number = ""
    while next_char and (next_char.isdigit() or next_char == '.'):
        number += next_char
        input.__next__()
        next_char = input.peek()
    return float(number)


def parse_string(input: Peekable[str], word: str) -> bool:
    next_char = input.peek()
    matched = 0
    while next_char and matched < len(word):
        print(f"string {next_char}")
        if next_char == word[matched]:
            matched += 1
            input.__next__()
            next_char = input.peek()
        else:
            return False
    return matched == len(word)


def parse_between[T](input: Peekable[str], opening: str, closing: str, func: Callable[[Peekable[str]], List[T]]) -> List[T]:
    next_char = input.peek()
    matched_opening = False
    result = []
    if not next_char:
        raise ValueError()
    while next_char:
        print(f"between {next_char}")
        match next_char:
            case a if a == opening[0] and not matched_opening:
                if not parse_string(input, opening):
                    raise ValueError("Couldnt parse opening tag")
                matched_opening = True
                result = func(input)
                next_char = input.peek()
            case a if a == closing[0] and matched_opening:
                if not parse_string(input, closing):
                    raise ValueError("Couldnt parse closing tag")
                return result
            case ' ' | '\t' | '\n':
                input.__next__()
                next_char = input.peek()
            case _ if matched_opening:
                input.__next__()
                next_char = input.peek()
            case _ if not matched_opening:
                raise ValueError()
    raise ValueError()


def parse_items(input: Peekable[str]):
    next_char = input.peek()
    result = []
    while next_char:
        print(f" items {next_char}")
        match next_char:
            case a if a.isdigit() or a == '.':
                result.append(parse_number(input))
                next_char = input.peek()
            case a if a == '[':
                result.append(parse_list(input))
                next_char = input.peek()
            case a if a == ']':
                return result
            case _:
                input.__next__()
                next_char = input.peek()
    return result


def parse_list(input: Peekable[str]) -> List[float] | float:
    next_char = input.peek()
    while next_char:
        print(f"list {next_char}")
        match next_char:
            case a if a.isdigit() or a == '.':
                return parse_number(input)
            case a if a == '[':
                return parse_between(input, '[', ']', parse_items)
            case _:
                input.__next__()
                next_char = input.peek()
    raise ValueError


def parse(input: str) -> List[float] | float:
    return parse_list(Peekable(input))


def main() -> None:
    while True:
        inp = input(">>")
        print(parse(inp))


if __name__ == "__main__":
    main()
