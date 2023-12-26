#!/bin/bash
INPUT_FILE=../data/nyc_311_limit.prepped.csv
OUTPUT_FILE=../data/nyc_311_limit.2020.csv

cat ${INPUT_FILE} | csvgrep -c 2 -r "^\d{2}/\d{2}/2020.*" > ${OUTPUT_FILE}