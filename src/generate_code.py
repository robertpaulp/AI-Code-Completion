import csv
from pandas import DataFrame
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("bigcode/tiny_starcoder_py")
model = AutoModelForCausalLM.from_pretrained("bigcode/tiny_starcoder_py")

def read_dataset(filename):
    dataset = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            dataset.append(row)
    return dataset

def generate_code(prefix, suffix):
    input = '<fim_prefix>' + prefix + '<fim_suffix>' + suffix + '<fim_middle>'
    inputs = tokenizer.encode(input, return_tensors='pt')
    outputs = model.generate(inputs, max_length=200)
    
    return tokenizer.decode(outputs[0])

def main():
    dataset = read_dataset('dataset.csv')

    print('Generating completions...')
    print(len(dataset))

    # Write completions to a file
    generation = DataFrame(columns=['prefix', 'middle', 'generated code', 'suffix'])
    for prefix, current, suffix in dataset:
        generated = generate_code(prefix, suffix)
        generation.loc[len(generation.index)] = [prefix, current, generated, suffix]

    generation.to_excel('generation.xlsx', index=False)

if __name__ == '__main__':
    main()
