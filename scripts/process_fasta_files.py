#!/usr/bin/env python3
import argparse
import random

def simplify_fasta(file_path):
    with open(file_path, 'r') as f:
        data = f.read()

    simplified = []
    entries = [entry for entry in data.split('>sp') if entry.strip()]

    for entry in entries:
        lines = entry.split('\n')
        identifier = lines[0].split('|')[1] if '|' in lines[0] else lines[0]
        sequence = ''.join(lines[1:]).replace('\n', '')
        simplified_entry = f'>{identifier}\n{sequence}'
        simplified.append(simplified_entry)

    output_content = '\n\n'.join(simplified)
    output_file_path = file_path.rsplit('.', 1)[0] + '_simple.' + file_path.rsplit('.', 1)[1]

    with open(output_file_path, 'w') as output_file:
        output_file.write(output_content)

    print(f'File saved as {output_file_path}')
    return output_file_path

def shuffle_fasta(data):
    entries = data.strip().split('\n>')
    entries = [entry if entry.startswith('>') else '>' + entry for entry in entries]
    random.shuffle(entries)
    return '\n\n'.join(entry.strip() for entry in entries)

def process_fasta_files(positive_path, negative_path, training_portion):
    print('-' * 40)
    positive_simplified_path = simplify_fasta(positive_path)
    negative_simplified_path = simplify_fasta(negative_path)

    with open(positive_simplified_path, 'r') as file:
        simplified_positive = file.read()
    with open(negative_simplified_path, 'r') as file:
        simplified_negative = file.read()

    shuffled_positive = shuffle_fasta(simplified_positive)
    shuffled_negative = shuffle_fasta(simplified_negative)

    pos_entries = shuffled_positive.split('\n\n')
    neg_entries = shuffled_negative.split('\n\n')

    split_index_pos = int(len(pos_entries) * training_portion)
    split_index_neg = int(len(neg_entries) * training_portion)

    pos_train_data = pos_entries[:split_index_pos]
    pos_test_data = pos_entries[split_index_pos:]
    neg_train_data = neg_entries[:split_index_neg]
    neg_test_data = neg_entries[split_index_neg:]

    random.shuffle(pos_train_data)
    random.shuffle(pos_test_data)
    random.shuffle(neg_train_data)
    random.shuffle(neg_test_data)

    base_name = positive_path.rsplit('.', 1)[0].replace('_pos', '')
    pos_train_file_name = f'{base_name}_pos_train.fasta'
    pos_test_file_name = f'{base_name}_pos_test.fasta'
    neg_train_file_name = f'{base_name}_neg_train.fasta'
    neg_test_file_name = f'{base_name}_neg_test.fasta'

    with open(pos_train_file_name, 'w') as file:
        file.write('\n\n'.join(pos_train_data))
    with open(pos_test_file_name, 'w') as file:
        file.write('\n\n'.join(pos_test_data))
    with open(neg_train_file_name, 'w') as file:
        file.write('\n\n'.join(neg_train_data))
    with open(neg_test_file_name, 'w') as file:
        file.write('\n\n'.join(neg_test_data))

    print('Training and testing datasets have been saved.')

def main():
    parser = argparse.ArgumentParser(description='Process FASTA files to prepare machine learning datasets.')
    parser.add_argument('positive_path', help='Path to the positive FASTA file.')
    parser.add_argument('negative_path', help='Path to the negative FASTA file.')
    parser.add_argument('training_portion', type=float, help='Portion of data to use for training (0-1).')

    args = parser.parse_args()
    process_fasta_files(args.positive_path, args.negative_path, args.training_portion)

if __name__ == "__main__":
    main()
