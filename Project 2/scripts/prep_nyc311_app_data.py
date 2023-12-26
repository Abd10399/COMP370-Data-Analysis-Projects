import argparse
import sys
import pandas as pd

INCIDENT_ZIP = "Incident Zip"
OPENED_AT_COLUMN_NAME = "Created Date"
CLOSED_AT_COLUMN_NAME = "Closed Date"
DURATION_COLUMN_NAME = "Duration"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-o", "--output", help="The output file to write to", default="stdout"
    )
    parser.add_argument(
        "file", help="A csv containing zipcode, opening date, closing date"
    )

    args = parser.parse_args()

    # load the file
    sys.stderr.write("loading data\n")
    df = pd.read_csv(args.file)

    # add a new column containing the difference between open and close times
    sys.stderr.write("converting dates\n")
    df[OPENED_AT_COLUMN_NAME] = pd.to_datetime(df[OPENED_AT_COLUMN_NAME])
    df[CLOSED_AT_COLUMN_NAME] = pd.to_datetime(df[CLOSED_AT_COLUMN_NAME])

    sys.stderr.write("Creating duration column\n")
    df[DURATION_COLUMN_NAME] = df[CLOSED_AT_COLUMN_NAME] - df[OPENED_AT_COLUMN_NAME]
    df[DURATION_COLUMN_NAME] = df[DURATION_COLUMN_NAME].dt.total_seconds() / 60 / 60

    # modify the opened date to be just the the month
    sys.stderr.write("extracting month\n")
    df[OPENED_AT_COLUMN_NAME] = df[OPENED_AT_COLUMN_NAME].dt.month

    # only keep incident zip and duration columns
    sys.stderr.write("dropping columns\n")
    df = df[[INCIDENT_ZIP, OPENED_AT_COLUMN_NAME, DURATION_COLUMN_NAME]]

    # drop all rows that have a NaN in the duration column
    df = df.dropna(subset=[DURATION_COLUMN_NAME])

    # collapse by zipcode and opened at
    sys.stderr.write("Collapsing and aggregating\n")
    df = df.groupby([INCIDENT_ZIP, OPENED_AT_COLUMN_NAME]).agg(
        {DURATION_COLUMN_NAME: "mean"}
    )

    # convert zip into an int
    # print("Converting zip")
    # df[INCIDENT_ZIP] = df[INCIDENT_ZIP].astype(int)

    # write csv format
    if args.output != "stdout":
        df.to_csv(args.output)
    else:
        print(df.to_csv())


if __name__ == "__main__":
    main()
