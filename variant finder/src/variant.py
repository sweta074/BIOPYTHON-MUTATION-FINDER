import Bio
# print (Bio.__version__)
from Bio.SeqIO import parse
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq
from Bio.Data import IUPACData
from Bio.Seq import transcribe
from Bio.Seq import translate
from Bio.Data import CodonTable
from Bio.SeqIO import write
from Bio import SeqIO
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio import AlignIO
from Bio import Align
from pathlib import Path
import csv


BASE_DIR = Path(__file__).resolve().parent.parent
ref_path = BASE_DIR / "data" / "ref.fasta"
samples_path = BASE_DIR / "data" / "sample.fasta"


file = open(ref_path)
for record in parse(file,"fasta"): 
    print(record.id)
    print(record.seq)

file1 = open(samples_path)
for record in parse(file1,"fasta"): 
    print(record.id)
    print(record.seq)

aligner = Align.PairwiseAligner()
aligner.mode = "global"
aligner.match_score = 1.0
aligner.mismatch_score = 0.0

aligner.open_gap_score = -1.0
aligner.extend_gap_score = -1.0

ref_record = SeqIO.read(ref_path, "fasta")
all_mutations = []



for sample_record in SeqIO.parse(samples_path,'fasta'):
    alignments = aligner.align(ref_record.seq, sample_record.seq)
    best_alignment = alignments[0]
    print(best_alignment)
    print(sample_record.id)
    print(best_alignment.score)
    aligned_ref = best_alignment[0]
    aligned_sample = best_alignment[1]
    print(aligned_ref)
    print(aligned_sample)
    ref_pos = 0
    for ref_base, sample_base in zip(aligned_ref, aligned_sample):
        if ref_base=="-":
            print(f"Insertion of {sample_base} after position {ref_pos}")
            all_mutations.append([sample_record.id, "Insertion", ref_pos, ref_base, sample_base])
        elif sample_base == "-":
            ref_pos += 1
            print(f"Deletion: del{ref_pos}{ref_base}")
            all_mutations.append([sample_record.id, "Deletion", ref_pos, ref_base, sample_base])
        elif ref_base != sample_base:
            ref_pos += 1
            print(f"Substitution: {ref_base}{ref_pos}{sample_base}")
            all_mutations.append([sample_record.id, "Substitution", ref_pos, ref_base, sample_base])
        else:
            ref_pos+=1
    

output_path = BASE_DIR / "readme" / "mutations.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sample_ID", "Type", "Position", "Ref_Base", "Sample_Base"])
    writer.writerows(all_mutations)



print(f"Done! Found {len(all_mutations)} mutations. Saved to {output_path}")






    













