#!/usr/bin/env python3
import argparse

def clean_msa(path, first_clipping_num, output_file_name):
    """
    Clean MSA file by removing specified number of characters from the beginning of each sequence.
    """
    print('-' * 40)
    print(f'Reading MSA file from {path}...')
    with open(path) as f:
        fastas = f.read().strip().split('\n\n')
    print(f'Number of sequences found: {len(fastas)}')
    print('-' * 40)

    clean_list = []
    for fasta in fastas:
        id = fasta.split()[0]
        sequence = ''.join(fasta.split('\n')[1:])
        clean_list.append((id, sequence[first_clipping_num:]))

    print(f'Removing the first {first_clipping_num} characters from each sequence...')
    with open(output_file_name + '.txt', 'w') as f:
        for item in clean_list:
            f.write(f"{item[0]}\n{item[1]}\n")
    print('-' * 40)
    print(f'Output saved in {output_file_name}.txt')
    print('-' * 40)

def main():
    parser = argparse.ArgumentParser(description='Clean MSA file by removing specified number of characters from the beginning of each sequence.')
    parser.add_argument('path', help='Path to the input MSA file.')
    parser.add_argument('first_clipping_num', type=int, help='Number of characters to remove from the beginning of each sequence.')
    parser.add_argument('output_file_name', help='Name of the output file.')

    args = parser.parse_args()
    clean_msa(args.path, args.first_clipping_num, args.output_file_name)

if __name__ == "__main__":
    main()
