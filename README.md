# IMEI-Compatibility-Filter

**A Python script which does the work of a VLOOKUP in Excel.**

_The script takes in two CSV files; these CSV files contain information about phone compatibility (i.e. what bands are available on a particular version of the phone). These files are used when you check on a provider's website to determine if you can use your phone on their network._

_The script filters through every row in both files, and will determine which rows are new in a given month. This information will then be output in a way that can be immediately uploaded to Skinny's phone compatibility checker._

## Getting Started

The application is built using Python 3.0. Download a version appropriate to your OS here: https://www.python.org/downloads/ 

### Prerequisites

Python 3.0.

## Background

_The intent of this application was to automate the process of filtering through CSV files to find non-duplicate rows and format them in a way I support understands. GSMa (https://www.gsma.com/services/gsma-imei/tac-allocation/) provide raw files with the information of every phone available, and the 3G/4G bands they support._

_The mobile provider I worked with had an IMEI Compatibility checker for their network which takes in a CSV file; this file needs to contain only the new phones (i.e. the "non-duplicated rows"), and requires headers and fields to be formatted very specifically._

_Previously, I used an Excel spreadsheet and compared fields using VLOOKUP. As I had a slow machine, this was a very slow process (it needed to go through 170,000 rows and filter out the fields that were already online). This application can filter through the same amount of information in 1.25 seconds, instead of multiple hours. The application does use three dictionaries to filter out the duplicated data, but given the data size of the CSV files being dealt with this wasn't causing any bottlenecks._

## Authors

- **David Coutts** - _Initial work_ - [bandicoutts](https://github.com/bandicoutts)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
