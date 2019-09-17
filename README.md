# IMEI-Compatibility-Filter
An application which will take in two CSV files, filter through every row in both files and remove duplicates, and return a CSV with the non-duplicated rows formatted in an acceptable way for the website which uses the file.

## Getting Started

The application is built using Python 3.0. Download a version appropriate to your OS here: https://www.python.org/downloads/

### Prerequisites

Python 3.0.

## Background

The intent of this application was to automate the process of filtering through CSV files to find non-duplicate rows and format them in a way I support understands. GSMa (https://www.gsma.com/services/gsma-imei/tac-allocation/) provide raw files with the information of every phone available, and the 3G/4G bands they support. 

The mobile provider I work with have an IMEI Compatibility checker for their network which takes in a CSV file; this file needs to contain only the new phones (i.e. the "non-duplicated rows"), and requires headers and fields to be formatted very specifically.

Previously, I used an Excel spreadsheet which would take roughly an hour to go through 170,000 rows and filter out the fields that were already online; this application can filter through the same amount of information in 1.25 seconds. The application does use three dictionaries to filter out the duplicated data, but given the data size of the CSV files being dealt with this wasn't causing any bottlenecks.

## Authors

* **David Coutts** - *Initial work* - [bandicoutts](https://github.com/bandicoutts)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
