# Description
This project touches upon data visualization using Bokeh dashboards and matplotlib to allow New York city leaders to explore the discrepancy in service across zipcodes. This would allow us to infer bias in the handling of service requests across the city of New York.

We create scripts to allow data manipulation and pre processing before doing our analytical work.
## Setup
Set PYTHONPATH to include the `src` dir.

## Running

Notably, nyc_311_limit.csv doesn't come with headers in it. So we need to grab them from somewhere. We got them from the website where the dataset originated.

Add headers to the csv data: `add_header.sh`

Next we trim the data down to 2020: `trim_to_2020.sh`

Compile borough complaints: `borough_complaints.py ...`

