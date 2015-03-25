import csv

def get_data():
	data = csv.DictReader(open("api.csv"))
	results = {"Work History": []}
	for line in data:
		results["Work History"].append({
			"Company": line["Company"],
			"Position": line["Position"],
			"Date": line["Date"],
			"Experience": line["Experience"]
			})
	return results