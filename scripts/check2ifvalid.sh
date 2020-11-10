#!/bin/bash

filename=$1
n=1
while read line; do
# reading each line

echo "Line number: $n"
echo $line | jsonlint-php 

#echo "Line No. $n : $line"
n=$((n+1))
done < $filename 
