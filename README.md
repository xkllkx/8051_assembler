# 8051 Assembler
This repository implements an assembler for the 8051 microcontroller, focusing on the functionality for XRL, DEC, and CJNE instructions.
The assembler reads instructions from a specified input file, processes them, and outputs the corresponding machine code.

# How to use this repo
Run the example script to see the real-time plot in action.
```bash
python assembler.py
```

# Example
Given an assembly code file testcase/test01.txt containing:
```txt
XRL   47H, A
DEC   A
DEC   @R0
CJNE  R2,  #37H,  16H
```
Running the assembler with the document number 1 will produce the following output:
```txt
輸入要組譯的文檔編號：
1
['XRL', '47H', 'A'] >> 62 47
['DEC', 'A'] >> 14
['DEC', '@R0'] >> 16
['CJNE', 'R2', '#37H', '16H'] >> BA 37 16 
----------------------------------        
MC: 62 47 14 16 BA 37 16
```
