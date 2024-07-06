from collections.abc import Sequence
from typing import Callable, Iterator, List, Optional
from dataclasses import dataclass
import functools as f


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


def is_opening(s: str) -> str:
    match s:
        case '[': return ']'
        case '(': return ')'
        case '{': return '}'
        case '<': return '>'
        case _: return ''


def parse_between[T](input: Peekable[str], opening: str, closing: str, func: Callable[[Peekable[str]], List[T]]) -> List[T]:
    next_char = input.peek()
    matched_opening = False
    result = []
    while next_char:
        # print(f"between {next_char}")
        match next_char:
            case a if a == opening and not matched_opening:
                input.__next__()
                matched_opening = True
                result = func(input)
                next_char = input.peek()
            case a if a == closing and matched_opening:
                input.__next__()
                return result
            case ' ' | '\t' | '\n':
                input.__next__()
                next_char = input.peek()
            case _ if matched_opening:
                input.__next__()
                next_char = input.peek()
            case _ if not matched_opening:
                raise ValueError("Couldnt find opening tag ")
    raise ValueError("Couldnt find closing tag")


def parse_items(input: Peekable[str], closing: str):
    next_char = input.peek()
    result = []
    while next_char:
        match next_char:
            case a if a.isdigit() or a == '.':
                result.append(parse_number(input))
                next_char = input.peek()
            case a if is_opening(a):
                result.append(parse_list(input))
                next_char = input.peek()
            case a if a == closing:
                return result
            case _:
                input.__next__()
                next_char = input.peek()
    return result


def parse_list(input: Peekable[str]) -> List[float] | float:
    next_char = input.peek()
    while next_char:
        match next_char:
            case a if a.isdigit() or a == '.':
                return parse_number(input)
            case a if is_opening(a):
                return parse_between(input, a, is_opening(a), f.partial(parse_items, closing=is_opening(a)))
            case _:
                input.__next__()
                next_char = input.peek()
    raise ValueError("Couldnt find neither list nor any value")


def parse(input: str) -> List[float] | float:
    return parse_list(Peekable(input))


def parse_from_file(path: str) -> List[float] | float:
    with open(path, encoding="UTF-8") as f:
        return parse(f.read())


# def main() -> None:
#     while True:
#         inp = input(">>")
#         print(parse(inp))
#
#
# if __name__ == "__main__":
#     main()
