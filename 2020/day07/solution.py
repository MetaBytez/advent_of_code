# https://adventofcode.com/2020/day/7
from collections import defaultdict

class Bag:
    def __init__(self, adjective: str, color: str):
        self.adjective = adjective
        self.color = color
        self.contents: dict[Bag, int] = defaultdict(lambda: 0)

    def __eq__(self, other: object) -> bool:
        assert isinstance(other, Bag)
        return self.adjective == other.adjective and self.color == other.color

    def __len__(self):
        return 1 + sum([
            count * len(bag)
            for bag, count in self.contents.items()
        ])

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return self.adjective + ' ' + self.color + ' bag'

    def add_bags(self, bag: object, count: int) -> None:
        assert isinstance(bag, Bag)
        self.contents[bag] += count

    def contains(self, bag: object) -> bool:
        assert isinstance(bag, Bag)
        if bag in self.contents:
            return True

        for inner_bag in self.contents:
            if inner_bag.contains(bag):
                return True

        return False


def load_baggage(baggage: list[str]) -> dict[Bag, Bag]:
    bags: dict[Bag, Bag] = {}
    for line in baggage:
        outer, inner = line.split(' bags contain ')
        outer_bag = Bag(*outer.split())
        outer_bag = bags.setdefault(outer_bag, outer_bag)

        if inner == 'no other bags.':
            continue

        for descriptor in inner.split(', '):
            count, adjective, color, __ = descriptor.split()
            inner_bag = Bag(adjective, color)
            inner_bag = bags.setdefault(inner_bag, inner_bag)
            outer_bag.add_bags(inner_bag, int(count))

    return bags


def part_1() -> int:
    """265"""
    with open('input.txt') as f:
        bags = load_baggage(f.read().split('\n'))
        

    our_bag = Bag('shiny', 'gold')
    count = 0
    for bag in bags:
        if bag.contains(our_bag):
            count += 1
    return count

def count_bags(bag, bags):
    childern = bags[bag]
    if not childern:
        print(f'{bag} - 1')
        return 1

    total = 1
    for child in childern:
        count, *nested = child
        total += int(count)*count_bags(tuple(nested), bags)

    print(f'{bag} - {total}')    
    return total


def part_2() -> int:
    """14177"""
    with open('input.txt') as f:
        bags = load_baggage(f.read().split('\n'))

    return len(bags[Bag('shiny', 'gold')]) - 1


if __name__ == '__main__':
    print(part_1())
    print(part_2())
