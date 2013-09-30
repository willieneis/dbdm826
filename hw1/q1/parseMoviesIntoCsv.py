import sys

# parse movies file into csv
movieFileName = sys.argv[1]
outFileName = sys.argv[2]
row = []
with open(movieFileName) as infile:
    for line in infile:
        if len(line)>1:
            row.append(line.split(':')[-1].strip())
            if 'time' in line:
                with open(outFileName, "a") as outfile:
                        outfile.write(', '.join(map(str,row))+'\n')
                row = []
