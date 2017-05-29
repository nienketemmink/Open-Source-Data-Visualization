# pseudo code

import json

def main():
    with open('DM_json_orde_muziek.json', 'r') as inputFile:
    	data = json.load(inputFile)

trackList = []
keys = ["track_id", "track_listens", "track_downloads", "track_title", "artist_name"]

for track in data["atracks"]:
	trackdict = {}
	for k in keys:
		trackdict[k] = track[k]
	trackList.append(trackdict)

#
with open('tracks_data.json', 'w') as outputFile:
   	json.dump(trackList, outputFile, indent=2, sort_keys=True)
