from queries.MAG import *
from queries.BB import *
from utils.FunctionUtils import *
from datetime import date
from datetime import timedelta
from utils.Env import BBDBPassword, BBDBUserName, BBDBPORT
import json

ICEe = DBConnect(BBDBUserName, BBDBPassword, BBDBPORT)
cursorBB = ICEe.cursor()
path = '../Batches.json'
yesterday = date.today() - timedelta(1)


def get_batch(inptDate):
    getBatchQuery = ["""SELECT IQT.QUEUE_TYPE_DESC,SII.Batch_ID,SII.CRE_DTTM FROM ICE_Ingestion.STG_ICEIngestion SII 
    join ICE_Ingestion.INGS_QUEUE_TYPE IQT on SII.QUEUE_TYPE_ID = IQT.QUEUE_TYPE_ID where  SII.CRE_DTTM like "%{}%" 
    order by SII.Batch_ID; """.format(
        inptDate)]
    get_batch_result = queryRun(getBatchQuery, cursorBB)

    return get_batch_result[0]


batch = get_batch(yesterday)

batchList = []
for i in range(0, len(batch)):
    batchList.append(batch[i][0])

batchDict = {}
for i in range(0, len(batchList)):
    batchDict[batchList[i]] = []
    for j in range(0, len(batch)):
        if batch[j][0] == batchList[i]:
            batchDict[batchList[i]].append(batch[j][1])

finalJson = {yesterday.strftime("%Y-%m-%d"): batchDict}


def txtFile(inptDict):
    updDict = json.dumps(inptDict)
    with open(path, 'w') as f:
        f.write("%s\n" % updDict)


print(finalJson)
txtFile(finalJson)

queriesListMag = [magNOTE, magMortgage, magAppraisal, mag1003, magW9, magSSN, magCD]
queriesListBB = [classificationQuery, extractionQuery, ingestionBlobs]
resultListMag = queryRun(queriesListMag, cursorBB)
resultListBB = queryRun(queriesListBB, cursorBB)

if resultListBB[2]:
    ingestBlob = True
else:
    ingestBlob = False
dictBB = {}

bbClassificationDetails = ["CLASSIFICATIONBLOBS", "CLASSIFICATIONPAGES"]
bbExtractionDetails = ["EXTRACTIONBLOBS", "EXTRACTIONPAGES"]
blobBusterUpdate = ''
batchLoop = len(list(batchDict.keys()))
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
print('Batch Details Done')
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
print('BB Done')
dictMag = {}
magDoc = ["NOTE", "MORTGAGE", "APPRAISAL", "1003",  "W9", "SSN", "CD"]
for i in range(7):
    if len(resultListMag[i]) == 0:
        dictMag[magDoc[i]] = 0
    else:
        dictMag[magDoc[i]] = resultListMag[i][0][2]

magTable = ""
for i in range(0, len(magDoc)):
    magTable += '<tr>' + \
                '<td>' + magDoc[i] + '</td>' + \
                '<td>' + str(dictMag[magDoc[i]]) + '</td>' + \
                '</tr>'
print('MAG Done')
