gzip flag.txt
cat flag.txt.gz| python3 flip.py > flag.txt.zg
cat flag.txt.zg| python3 flip.py > flag.txt.gz
gunzip flag.txt.gz
