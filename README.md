# Email Harvester
Email Harvester is a Python script that extracts email addresses from a given URL. The script uses Regular Expressions to find all email addresses present in the HTML code of the webpage, and can either print the results to the console or save them as a JSON file.

## Installation

To run the script, you will need to have Python 3.x installed on your system, along with the following packages:
```
re
requests
argparse
json
```

To install these packages, run the following command:

```
pip install -r requirements.txt
```
## Usage

To use the script, simply run the following command in your terminal:
```
python email_harvester.py -u <url> [-w]
```
Replace <url> with the URL of the webpage from which you want to extract email addresses. The -w flag is optional, and can be used to save the results as a JSON file.
 
## Examples
  
To extract email addresses from the webpage https://example.com and print the results to the console, run:
  
```
python email_harvester.py -u https://example.com
```
 
To extract email addresses from the webpage https://example.com and save the results as a JSON file, run:
  
  ```
  python email_harvester.py -u https://example.com -w
  ```
  
### Thanks for using Email Harvester!
