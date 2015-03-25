import csv

def get_data():
	data = csv.DictReader(open("api.csv"))
	results = {"WorkHistory": []}
	for line in data:
		results["WorkHistory"].append({
			"Company": line["Company"],
			"Position": line["Position"],
			"Date": line["Date"],
			"Experience": line["Experience"]
			})
	return results