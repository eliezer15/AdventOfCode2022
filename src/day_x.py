def part_one(use_test_input: bool):
    pass

def part_two(use_test_input: bool):
    pass

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