#!/usr/bin/env python3
import pandas as pd
import argparse

def clean_csv_file(path, output_file_name, string_or_file='f', save_format='f'):
    """
    Reads and cleans a CSV file, providing options to return the cleaned data as a string or save it into a file.
    """
    print('-' * 40)
    print(f'Reading CSV file from {path}...')
    df = pd.read_csv(path)
    print(f'Initial number of records: {len(df)}')
    print('-' * 40)

    # Drop rows with missing 'Entity ID' and update 'Entity ID' format
    df = df.dropna(subset=['Entity ID'])
    print(f'Number of records after dropping missing Entity ID: {len(df)}')
    df['Entity ID'] = df['Entity ID'].str.split('_').str[0] + ':' + df['Auth Asym ID']
    df = df.drop(columns=['Auth Asym ID'])
    df = df.reset_index(drop=True)

    # Option to return the cleaned data as a string
    if string_or_file == 's':
        cleaned_data = '\n'.join(df['Entity ID'].values)
        print('-' * 40)
        print('Returning cleaned data as a string.')
        return cleaned_data

    # Option to save the cleaned data to a file
    elif string_or_file == 'f':
        if save_format == 'f':
            output_path = output_file_name + '.fasta'
            with open(output_path, 'w') as file:
                for idx, row in df.iterrows():
                    file.write(f"> {row['Entity ID']}\n{row['Sequence']}\n")
            print(f'Data saved to {output_path}')
        elif save_format == 'k':
            output_path = output_file_name + '.txt'
            with open(output_path, 'w') as f:
                f.write('\n'.join(df['Entity ID'].values))
            print(f'Data saved to {output_path}')
        print('-' * 40)
        return None

def main():
    parser = argparse.ArgumentParser(description='Cleans a CSV file and returns the data as a string or saves it to a file.')
    parser.add_argument('path', help='The path to the CSV file to be cleaned.')
    parser.add_argument('output_file_name', help='The name of the output file.')
    parser.add_argument('--string_or_file', choices=['s', 'f'], default='f',
                        help='Output as string (s) or file (f). Default is file (f).')
    parser.add_argument('--save_format', choices=['f', 'k'], default='f',
                        help='Format for saving the data: Fasta format (f) or keys (k). Default is Fasta format (f).')

    args = parser.parse_args()

    result = clean_csv_file(args.path, args.output_file_name, args.string_or_file, args.save_format)
    if result:
        print(result)

if __name__ == "__main__":
    main()
