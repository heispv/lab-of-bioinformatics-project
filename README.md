# Lab of Bioinformatics Project

## Overview

This project is part of the Laboratory of Bioinformatics I at the University of Bologna. The main aim is to build a Profile Hidden Markov Model (HMM) for the Kunitz-type protease inhibitor domain. These domains are active regions of proteins that inhibit protein-degrading enzymes, including examples like aprotinin (BPTI), Alzheimer's amyloid precursor protein (APP), and tissue factor pathway inhibitor (TFPI). The project focuses on using the HMM to determine the optimal e-value threshold for binary classification based on HMM search results.

## Project Description

### Main Aim
The primary goal is to construct a Profile HMM for the Kunitz-type protease inhibitor domain, starting from available structural information, and use it to find the optimal e-value threshold for binary classification in HMM searches.

### Specific Aims
1. Build a model for the Kunitz domain using structural information.
2. Determine the optimal e-value threshold for binary classification based on HMM search results.

## Repository Structure

- **Jupyter Notebook**: The main analysis and results are documented in `lab_final_project.ipynb`.
- **Scripts**: Python scripts for data preprocessing and analysis are located in the `scripts` directory.
- **README.md**: This document provides an overview and instructions for the project.

## Jupyter Notebook

### lab_final_project.ipynb

This notebook includes the following sections:
1. **Installing Dependencies**: Instructions for installing necessary packages.
2. **Get the 3D Structure**: Steps to retrieve the 3D structure of the Kunitz domain from PDB.
3. **Clean CSV File**: Procedures for cleaning and preprocessing CSV files.
4. **Get MSA**: Methods to obtain Multiple Sequence Alignment (MSA).
5. **Build HMM Based on Raw MSA**: Building a Profile HMM using the raw MSA data.
6. **Clean Raw MSA**: Cleaning the raw MSA to improve the model.
7. **Build HMM Based on Clean MSA**: Constructing a Profile HMM using the cleaned MSA.
8. **Get the Negative and Positive Data from NCBI**: Retrieving datasets for model validation.
9. **Run blastp to Find the Matches**: Using blastp to find matches in the data.
10. **HMM Search**: Conducting HMM searches for domain prediction.
11. **Discussion**: Analyzing and discussing the results.

## Scripts

The `scripts` directory contains the following Python scripts:
- **clean_csv_file.py**: Cleans and preprocesses CSV files.
- **clean_msa.py**: Cleans multiple sequence alignment files.
- **evaluate_thresholds.py**: Evaluates different thresholds for analyses.
- **filter_sequences.py**: Filters sequences based on criteria.
- **process_fasta_files.py**: Processes FASTA files for analysis.

### Usage

To run the scripts, navigate to the `scripts` directory and execute the desired script using Python. For example:
```bash
cd scripts
python clean_csv_file.py
```

## Dependencies

Ensure the following dependencies are installed:

### System Dependencies
- **HMMER**: Install the HMMER library and documentation.
  ```bash
  sudo apt-get install hmmer
  sudo apt-get install hmmer-doc
  ```
- **NCBI BLAST+**: Install the NCBI BLAST+ suite.
  ```bash
  sudo apt-get install ncbi-blast+
  ```

### Python Libraries
- pandas
- numpy
- matplotlib
- seaborn

Install the necessary Python packages using pip:
```bash
pip install pandas numpy matplotlib seaborn
```

## Getting Started

1. Clone the repository:
```bash
git clone https://github.com/heispv/lab-of-bioinformatics-project.git
```
2. Navigate to the project directory:
```bash
cd lab-of-bioinformatics-project
```
3. Run the Jupyter Notebook:
```bash
jupyter notebook lab_final_project.ipynb
```
4. Execute the cells in the notebook to reproduce the analysis.

## Project Details

### Building the Model
- **Structure Selection**: Retrieve available structures of the Kunitz domain from PDB.
- **Protein Alignment**: Perform structural alignment of selected domains using methods like PDBe-fold.
- **HMM Generation**: Train a profile HMM using the HMMER hmmbuild routine.
- **Validation**: Validate the HMM using a suitable dataset from UniProt/Swiss-Prot and compute scoring indexes.

### Analysis and Results
- **Prediction**: Optimize predictions by adjusting thresholds or refining alignments.
- **Threshold Optimization**: Determine the optimal e-value threshold for binary classification based on HMM search results.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact the project maintainer at peymanvahidi1998@gmail.com.

---

This README provides a comprehensive guide to understanding, setting up, and contributing to the bioinformatics lab project. For detailed code and analysis, refer to the `lab_final_project.ipynb` notebook and the scripts in the `scripts` directory.
