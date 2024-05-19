#!/usr/bin/env python3
import argparse

def filter_sequences(seq_file_path, ids_file_path, output_file_path):
    """
    Filters sequences from a FASTA file based on a list of excluded sequence IDs and saves them in a file.
    """
    print('-' * 40)
    print(f'Reading excluded sequence IDs from {ids_file_path}...')
    with open(ids_file_path, 'r') as f:
        excluded_ids = {line.strip().split('|')[1] for line in f}
    print(f'Number of excluded IDs: {len(excluded_ids)}')
    print('-' * 40)

    print(f'Reading sequences from {seq_file_path}...')
    with open(seq_file_path, 'r') as f:
        content = f.read().strip()
        sequences = content.split('>')[1:]
    print(f'Number of sequences found: {len(sequences)}')
    print('-' * 40)

    print(f'Filtering sequences and writing to {output_file_path}...')
    with open(output_file_path, 'w') as outfile:
        filtered_count = 0
        for sequence in sequences:
            header = sequence.split('\n', 1)[0]
            seq_id = header.split('|')[1]

            if seq_id not in excluded_ids:
                outfile.write(f'>{sequence}\n')
                filtered_count += 1
    print(f'Number of sequences written to output: {filtered_count}')
    print('-' * 40)
    print('Filtering process completed.')

def main():
    parser = argparse.ArgumentParser(description='Filters sequences from a FASTA file based on a list of excluded sequence IDs.')
    parser.add_argument('seq_file_path', help='The file path to the input FASTA file containing sequences to filter.')
    parser.add_argument('ids_file_path', help='The file path to the input file containing a list of sequence IDs to exclude.')
    parser.add_argument('output_file_path', help='The file path to save the filtered sequences.')

    args = parser.parse_args()
    filter_sequences(args.seq_file_path, args.ids_file_path, args.output_file_path)

if __name__ == "__main__":
    main()
