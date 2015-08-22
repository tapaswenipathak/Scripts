import sys
import json

# Read Input File
inputFile = open(sys.argv[1])
input = json.load(inputFile)
inputFile.close()

# If No Output File Found, Print on Console
if len(sys.argv) < 3:
    print json.dumps(input, sort_keys=False, indent=2)

# Otherwise Store The Output
else:
    outputFile = open(sys.argv[2], "w")
    json.dump(input, outputFile, sort_keys=False, indent=2)
    outputFile.close()
