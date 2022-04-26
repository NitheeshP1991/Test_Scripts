import sys
import re
import datetime
import time

startTime = time.time()
cnt = 0
cnt2 = 0
failCnt = 0
reCompile = re.compile("\s([^\s]*?)=\"(.*?)\"")
delimiterCharacterOut = ","

def writeCSVLine(line):
    x = reCompile.findall(line)
    a = dict((row[0], row[1]) for row in x)

    try:
        a['ts1'] = str(int(int(a['ts']) / 1000))
        x = str(datetime.datetime.fromtimestamp(float(a['ts1'])))[0:19]
        b = a['ts'] + ",\"" + x + "\"," + a['t'] + "," + a['lt'] + ",\"" + a['s'] + "\",\"" + a['lb'] + "\"," + a[
            'rc'] + ",\"" + a['rm'] + "\",\"" + a['tn'] + "\",\"" + a['dt'] + "\"," + a['by'] + ",\"" + a[
                'sc'] + "\"," + a['ec'] + ",\"" + a['ng'] + "\"," + a['na'] + ",\"" + a['hn'] + "\"," + a['in'] + "\n"
    except:
        return -1
    o.write(b)
    return 1

print("Splitting JTL file")

try:
    runArgv = sys.argv  # Save the command line
    jtlInfile = str(sys.argv[1])  # Name of JTL input file
    cvsOutfile = str(sys.argv[2])  # Name of CVS output file
    reFilter = str(sys.argv[3])  # Filter the labels (lb) for the filter

except:
    print("Error: Input format: <input file> <output file> <Filter by regular expression>")
    raise

try:
    f = open('../Jmeter_log1.jtl', "r")
    o = open(cvsOutfile, "w")

except:
    raise

print("Filtering on regular expression : " + reFilter)
cmpFilter = re.compile(reFilter)
# o.write("timestamp" + ",\""+ "datetime" + "\n")
o.write("timeStamp" + ",\"" + "datetime" + "\"," + "elapsed" + "," + "Latency" + ",\"" + "success" + "\",\"" + "label" + "\"," + "responseCode" + ",\"" + "responseMessage" + "\",\"" + "threadName" + "\",\"" + "dataType" + "\"," + "bytes" + ",\"" + "SampleCount" + "\"," + "ErrorCount" + ",\"" + "grpThreads" + "\"," + "allThreads" + ",\"" + "Hostname" + "\"," + "IdleTime" + "\n")

for line in f:
    try:
        if cmpFilter.search(line):
            returnVal = writeCSVLine(line)
            if returnVal < 0:
                failCnt += 1
            else:
                cnt2 += 1
    except:
        print('Error in line : ', cnt, line)
        raise
    cnt += 1

endTime = time.time()
print("Time taken : ", str(endTime - startTime))
print("Lines processed : ", cnt)
print("Lines that passed the filter : ", cnt2)
print("Lines skipped (error?) : ", failCnt)
f.close()
o.close()
