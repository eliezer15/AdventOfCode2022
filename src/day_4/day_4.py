'''
Space needs to be cleared before the last supplies can be unloaded from the ships, and so several Elves have been assigned the job of cleaning up sections of the camp. Every section has a unique ID number, and each Elf is assigned a range of section IDs.

However, as some of the Elves compare their section assignments with each other, they've noticed that many of the assignments overlap. To try to quickly find overlaps and reduce duplicated effort, the Elves pair up and make a big list of the section assignments for each pair (your puzzle input).

For example, consider the following list of section assignment pairs:

2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
For the first few pairs, this list means:

Within the first pair of Elves, the first Elf was assigned sections 2-4 (sections 2, 3, and 4), while the second Elf was assigned sections 6-8 (sections 6, 7, 8).
The Elves in the second pair were each assigned two sections.
The Elves in the third pair were each assigned three sections: one got sections 5, 6, and 7, while the other also got 7, plus 8 and 9.
This example list uses single-digit section IDs to make it easier to draw; your actual list might contain larger numbers. Visually, these pairs of section assignments look like this:

.234.....  2-4
.....678.  6-8

.23......  2-3
...45....  4-5

....567..  5-7
......789  7-9

.2345678.  2-8
..34567..  3-7

.....6...  6-6
...456...  4-6

.23456...  2-6
...45678.  4-8
Some of the pairs have noticed that one of their assignments fully contains the other. For example, 2-8 fully contains 3-7, and 6-6 is fully contained by 4-6. In pairs where one assignment fully contains the other, one Elf in the pair would be exclusively cleaning sections their partner will already be cleaning, so these seem like the most in need of reconsideration. In this example, there are 2 such pairs.

In how many assignment pairs does one range fully contain the other?
'''
from typing import List


def part_one(use_test_input: bool):
    fully_contained_pairs = []

    for line in __get_input_lines(use_test_input):
        line = line.strip()
        pairs = line.split(',')

        pair_1 = pairs[0].split('-')
        pair_2 = pairs[1].split('-')

        if __is_fully_contained(pair_1, pair_2) or __is_fully_contained(pair_2, pair_1):
            fully_contained_pairs.append(line)
        
    return len(fully_contained_pairs)


def __is_fully_contained(pair_1: List, pair_2: List):
    # Don't forget to compare the Int version of the numbers and not the string!!!!
    return int(pair_1[0]) <= int(pair_2[0]) and int(pair_1[1]) >= int(pair_2[1])

'''
It seems like there is still quite a bit of duplicate work planned. Instead, the Elves would like to know the number of pairs that overlap at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and 2-6,4-8) do overlap:

5-7,7-9 overlaps in a single section, 7.
2-8,3-7 overlaps all of the sections 3 through 7.
6-6,4-6 overlaps in a single section, 6.
2-6,4-8 overlaps in sections 4, 5, and 6.
So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
'''
def part_two(use_test_input: bool):
    fully_contained_pairs = []

    for line in __get_input_lines(use_test_input):
        line = line.strip()
        pairs = line.split(',')

        pair_1 = pairs[0].split('-')
        pair_2 = pairs[1].split('-')

        if __overlaps(pair_1, pair_2):
            fully_contained_pairs.append(line)
        
    return len(fully_contained_pairs)

def __overlaps(pair_1: List, pair_2: List):
    start_1 = int(pair_1[0])
    end_1 = int(pair_1[1])

    start_2 = int(pair_2[0])
    end_2 = int(pair_2[1])

    if start_1 < start_2:
        return end_1 >= start_2
    
    elif start_1 > start_2:
        return end_2 >= start_1
    
    else:
        return True

def __get_input_lines(use_test_input: bool):
    filename = 'test_input.txt' if use_test_input else 'input.txt'
    with open(filename, 'r') as file:
        return file.readlines()

def main():
    print(f'Part one test result: {part_one(True)}')
    print(f'Part one real result: {part_one(False)}')
    print(f'Part two test result: {part_two(True)}')
    print(f'Part two real result: {part_two(False)}')

if __name__ == '__main__':
    main()