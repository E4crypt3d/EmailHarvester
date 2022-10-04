import re
import requests
import argparse
import json

def get_url(url):
	check_url = requests.get(url)
	if check_url.status_code != 200:
		print("Please check your URL")
		exit()
	else:
		return check_url.text

def get_regex():
	regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	return regex

def harvest_emails(url,save):
	regex = get_regex()
	try:
		exracted_emails = re.findall(regex,get_url(url))
		if len(exracted_emails) >= 1:
			if save:
				save_emails(exracted_emails)
				return "Look for the emails.json file in the same directory."
			else:
				get_emails(exracted_emails)
				return "Available Emails Found in the URL"
		else:
			return "No Emails Found"
	except Exception:
		return "Something Went wrong Please try again or check ur url"

def get_emails(exracted_emails):
	for no, em in enumerate(exracted_emails):
		print(f"{no} = {em}")

def save_emails(exracted_emails):
	emails = {}
	for no, email in enumerate(exracted_emails):
		emails[no] = [email]
	jmail = json.dumps(emails)
	with open("emails.json",'w') as mailfile:
		mailfile.write(jmail)
	

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-w',help="To save it as a JSON file if not provided it will only print in console or cmd", action="store_true")
	parser.add_argument('-u',help="Provide your url", type=str)
	args = parser.parse_args()
	results = harvest_emails(args.u, args.w)
	print(results)

if __name__ == '__main__':
	main()