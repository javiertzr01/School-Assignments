#!/bin/bash
for((i=0;i<256;i++))
do
	python3 ex2.py -i flag -o $i -k $i -m d
done
