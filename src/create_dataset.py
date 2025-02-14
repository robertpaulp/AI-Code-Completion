import random
import os
import csv

def split_code(code, cursor_pos):
    start = code.rfind('def ', 0, cursor_pos)
    end = code.find('def ', cursor_pos + 20)
    
    if start == -1:
        start = 0
    if end == -1:
        end = len(code)
    
    prefix = code[start:cursor_pos].rstrip()
    current = code[cursor_pos:cursor_pos + 20]
    suffix = code[cursor_pos + 20:end].lstrip()

    return prefix, current, suffix

def create_dataset(directory):
    dataset = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r') as file:
            code = file.read()

            for cursor_pos in range(0, len(code), 20):
                prefix, current, suffix = split_code(code, cursor_pos)
                if len(prefix) == 0 or len(suffix) == 0:
                    continue
                dataset.append((prefix, current, suffix))

    return dataset

def main():
    dataset = create_dataset('data/raw')
    dataset = random.sample(dataset, 50)

    with open('dataset.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['prefix', 'current', 'suffix'])
        for row in dataset:
            writer.writerow(row)

if __name__ == '__main__':
    main()