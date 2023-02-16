from MailQueriesMag import *
from MailQueriesBB import *
from GetBatchDB import *
from CommonFunction import *
from env import BBDBPassword, BBDBUserName
ICEe = DBConnect(BBDBUserName, BBDBPassword, "3388")
cursorBB = ICEe.cursor()

queriesListMag = [magNOTE, magMortgage,magAppraisal, mag1003, magW9, magSSN, magCD]
queriesListBB = [classificationQuery, extractionQuery, ingestionBlobs]
resultListMag = []
resultListBB = []
resultListMag = queryRun(queriesListMag, cursorBB)

resultListBB = queryRun(queriesListBB, cursorBB)

if resultListBB[2]:
    ingestBlob = True
else:
    ingestBlob = False
dictBB = {}

bbClassificationDetails = [
    "CLASSIFICATIONBLOBS",
    "CLASSIFICATIONPAGES"
]

bbExtractionDetails = [
    "EXTRACTIONBLOBS",
    "EXTRACTIONPAGES"
]

blobBusterUpdate = ''

batchLoop = len(list(batchDict.keys()))
print(batchLoop)
if batchLoop:
    for i in range(0, batchLoop):
        blobBusterUpdate += 'Batch ' + \
                            str(batchDict[list(batchDict.keys())[i]]) + ' in ' + \
                            list(batchDict.keys())[i] + ',\n'
    blobBusterUpdate = blobBusterUpdate.replace("[", "").replace("]", "") + "uploaded in last 24 hours."

elif batchLoop == 0:
    blobBusterUpdate += "No batches were uploaded in last 24 hour."

if ingestBlob:
    blobBusterUpdate += "Blobs are still in progress"
else:
    blobBusterUpdate += "No more blobs yet to be ingested"
print(resultListBB)
for i in range(2):
    dictBB[bbClassificationDetails[i]] = 0
    if resultListBB[0]:
        dictBB[bbClassificationDetails[i]] = resultListBB[0][0][i]
    dictBB[bbExtractionDetails[i]] = 0
    if resultListBB[1]:
        dictBB[bbExtractionDetails[i]] = resultListBB[1][0][i]
if resultListBB[0]:
    throughput = resultListBB[0][0][2]
else:
    throughput = 0
dictMag = {}

magDoc = [
    "NOTE",
    "MORTGAGE",
    "APPRAISAL",
    "1003",
    "W9",
    "SSN",
    "CD"]

dictFlow = {}

for i in range(7):
    if len(resultListMag[i]) == 0:
        dictMag[magDoc[i]] = 0
    else:
        dictMag[magDoc[i]] = resultListMag[i][0][2]

print(dictBB)
print(dictFlow)
print(dictMag)
print(resultListBB[1])
print("Blobs in progress - ", ingestBlob)
print(blobBusterUpdate)
print("Throughput-", throughput)
