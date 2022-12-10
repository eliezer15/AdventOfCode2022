from typing import List
import re

'''
The expedition can depart as soon as the final supplies have been unloaded from the ships. Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between stacks. To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. After the crates are rearranged, the desired crates will be at the top of each stack.

The Elves don't want to interrupt the crane operator during this delicate procedure, but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, so the first crate to be moved (D) ends up below the second and third crates:

        [Z]
        [N]
    [C] [D]
    [M] [P]
 1   2   3
Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

        [Z]
        [N]
[M]     [D]
[C]     [P]
 1   2   3
Finally, one crate is moved from stack 1 to stack 2:

        [Z]
        [N]
        [D]
[C] [M] [P]
 1   2   3
The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top of each stack?
'''
def part_one():
    stacks = __initialize_stacks()
    
    # start processing the moving instructions
    lines = get_input_lines()
    instructions_start_index = __get_instructions_start_index(lines)

    pattern = re.compile(r'^move (\d+) from (\d) to (\d)')
    for i in range(instructions_start_index, len(lines)):
        instruction = lines[i]
        matches = pattern.match(instruction)

        number_of_crates_to_move = int(matches.group(1))
        source_stack_number = int(matches.group(2))
        target_stack_number = int(matches.group(3))

        # the instructions start at 1, arrays start at 0
        source_stack = stacks[source_stack_number - 1]
        target_stack = stacks[target_stack_number - 1]
        for _ in range(number_of_crates_to_move):
            crate = source_stack.pop()
            target_stack.append(crate)

    result: List[str] = []
    for stack in stacks:
        result.append(stack.pop())
    
    print(f'The result is {"".join(result)}')

def __initialize_stacks() -> List[List]:
    number_of_stacks = 9
    characters_per_stack = 4

    # A deque works here, but using a List and reversing it at the end because part two is easier to work with a list

    stacks: List[List] = []

    for _ in range(number_of_stacks):
        stacks.append([])

    for line in get_input_lines():        
        # Process input only on the top stack portion
        if line.startswith(' 1'):
            break

        for stack in range(number_of_stacks):

            # the relevant letter is the second character from the current index
            # times chars per stack to match the expected string location

            crate = line[stack * characters_per_stack + 1]
            if not crate.isspace():
                stacks[stack].append(crate)
    
    for stack in stacks:
        stack.reverse()

    return stacks

def __get_instructions_start_index(lines: List[str]) -> int:
    for i in range(len(lines)):
        if lines[i].startswith('move'):
            return i

'''
As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you quickly wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, and the ability to pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same configuration:

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 
Moving a single crate from stack 2 to stack 1 behaves the same as before:

[D]        
[N] [C]    
[Z] [M] [P]
 1   2   3 
However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, resulting in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3
Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3
Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3
In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?
'''
def part_two():
    stacks = __initialize_stacks()
    
    # start processing the moving instructions
    lines = get_input_lines()
    instructions_start_index = __get_instructions_start_index(lines)

    pattern = re.compile(r'^move (\d+) from (\d) to (\d)')
    for i in range(instructions_start_index, len(lines)):
        instruction = lines[i]
        matches = pattern.match(instruction)

        number_of_crates_to_move = int(matches.group(1))
        source_stack_number = int(matches.group(2))
        target_stack_number = int(matches.group(3))

        # the instructions start at 1, arrays start at 0
        source_stack = stacks[source_stack_number - 1]
        target_stack = stacks[target_stack_number - 1]

        lowest_crate_to_move_index = len(source_stack) - number_of_crates_to_move

        # Pop by getting and deleting
        crates_to_move = source_stack[lowest_crate_to_move_index:]
        del source_stack[lowest_crate_to_move_index:]        

        target_stack.extend(crates_to_move)

    result: List[str] = []
    for stack in stacks:
        result.append(stack.pop())
    
    print(f'The result is {"".join(result)}')

def get_input_lines():
    with open('input.txt', 'r') as file:
        return file.readlines()

def main():
    part_one()
    part_two()

if __name__ == '__main__':
    main()