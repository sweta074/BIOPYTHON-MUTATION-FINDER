PROJECT = BIOPYTHON MUTATION FINDER
ABOUT   = A Python script that compares sample DNA sequences against a reference FASTA file to find substitutions, insertions, and deletions. It uses Biopython (Bio.SeqIO and Bio.Align) to align sequences, tracks 1-based reference positions across gaps, and saves all detected mutations into a clean CSV table. Tested on human HBB (beta-globin) sequences from NCBI.


variant finder/
|-- data/
|   |--ref.fasta                #Reference Human HBB sequence from NCBI NM_000518.5
|   |--sample.fasta             #Sample sequences to compare   
|
|--readme/
|  |--mutations.csv
|
|--src/
|  |--variant.py
|
|--About.md



## Example Output (readme/mutations.csv)

Sample_ID	Type	Position	Ref_Base	Sample_Base
M25079.1	Deletion	2	C	-
M25079.1	Deletion	3	A	-
AF181832.1	Deletion	26	T	-
AF181832.1	Deletion	27	C	-
AF181832.1	Deletion	29	C	-
AY136510.1	Deletion	30	T	-
AY136510.1	Deletion	31	A	-

