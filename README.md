# TOC-cfg-ast-Plagarism-Detection
The aim of this project is to design and implement a plagiarism detection system based on formal language theory concepts, specifically Context Free Grammars (CFG), Pushdown Automata (PDA), and Parse Trees.
Traditional plagiarism detectors rely heavily on string matching or token matching, which can easily be bypassed by modifying variable names, formatting, or comments. This project instead analyzes the syntactic structure of programs by parsing them into Abstract Syntax Trees (ASTs) derived from CFG rules.
By comparing structural similarities between programs, the system can detect plagiarism even when superficial changes are made.
The system will:
Parse programs written in Python or C (subset grammar).
Generate parse trees using CFG rules.
Compare syntax trees to detect structural similarities.
Produce a similarity score along with highlighted plagiarized segments.
This project demonstrates how formal language theory can be applied to real-world problems in education and code analysis.

