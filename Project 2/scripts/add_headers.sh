#!/bin/bash
INPUT_FILE=../data/nyc_311_limit.csv
OUTPUT_FILE=../data/nyc_311_limit.prepped.csv

cat ../data/headers.txt | sed 's/^[ \t]*//;s/[ \t]*$//' | tr '\n' ',' > ${OUTPUT_FILE}
echo >> ${OUTPUT_FILE}
cat ${INPUT_FILE} >> ${OUTPUT_FILE}