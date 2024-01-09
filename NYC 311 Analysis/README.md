# Setup
Set PYTHONPATH to include the `src` dir.

# Running

Notably, nyc_311_limit.csv doesn't come with headers in it. So we need to grab them from somewhere. We got them from the website where the dataset originated.

Add headers to the csv data: `add_header.sh`

Next we trim the data down to 2020: `trim_to_2020.sh`

Compile borough complaints: `borough_complaints.py ...`

