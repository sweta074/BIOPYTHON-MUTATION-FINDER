# BIOPYTHON-MUTATION-FINDER
Compares sample DNA sequences against a reference FASTA file to find substitutions, insertions, and deletions. It uses Biopython (Bio.SeqIO and Bio.Align) to align sequences, tracks 1-based reference positions across gaps, and saves all detected mutations into a clean CSV table. Tested on human HBB (beta-globin) sequences from NCBI.
