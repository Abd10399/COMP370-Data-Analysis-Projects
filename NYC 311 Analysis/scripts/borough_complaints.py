#!python3
from argparse import ArgumentParser
import pandas as pd
from datetime import datetime
import logging

from nyc311_constants import Nyc311ColumnName

logger = logging.getLogger(__name__)


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-i", "--input", required=True, help="the nyc 311 csv file to process"
    )
    parser.add_argument(
        "-s", "--start_date", required=True, help="the start date to filter"
    )
    parser.add_argument(
        "-e", "--end_date", required=True, help="the end date to filter"
    )
    parser.add_argument(
        "-o", "--output", default=None, help="the output file to write to"
    )

    args = parser.parse_args()

    fname = args.input

    # need to be careful using a dataframe here because the data file could be huge
    logger.info(f"Reading {fname}")
    df = pd.read_csv(fname)

    # filter by the date range
    fmt_string = "%Y.%m.%d"
    start_date = datetime.strptime(args.start_date, fmt_string)
    end_date = datetime.strptime(args.end_date, fmt_string)

    logger.info(f"Filtering by date range {args.start_date} to {args.end_date}")
    nyc311_fmt_string = "%m/%d/%Y %I:%M:%S %p"
    df[Nyc311ColumnName.OpenedDate.value] = pd.to_datetime(
        df[Nyc311ColumnName.OpenedDate.value], format=nyc311_fmt_string
    )
    df = df[
        (df[Nyc311ColumnName.OpenedDate.value] >= start_date)
        & (df[Nyc311ColumnName.OpenedDate.value] <= end_date)
    ]

    # now compile frequency info
    logger.info("Compiling borough frequency info")
    df = (
        df.groupby(
            [Nyc311ColumnName.Borough.value, Nyc311ColumnName.ComplaintType.value]
        )
        .size()
        .reset_index(name="count")
    )

    if args.output is not None:
        df.to_csv(args.output, index=False)
    else:
        print(df.to_csv(index=False))


if __name__ == "__main__":
    main()
