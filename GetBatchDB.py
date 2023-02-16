from datetime import date
from datetime import timedelta
from CommonFunction import queryRun, DBConnect
from env import BBDBPassword, BBDBUserName
import json

ICEe = DBConnect(BBDBUserName, BBDBPassword, "3388")
cursorBB = ICEe.cursor()

path = 'Batches.json'
yesterday = date.today() - timedelta(1)


def get_batch(inptDate):
    getBatchQuery = ["""SELECT IQT.QUEUE_TYPE_DESC,SII.Batch_ID,SII.CRE_DTTM FROM ICE_Ingestion.STG_ICEIngestion SII join ICE_Ingestion.INGS_QUEUE_TYPE IQT on SII.QUEUE_TYPE_ID = IQT.QUEUE_TYPE_ID where  SII.CRE_DTTM like "%{}%" order by SII.Batch_ID; """.format(
        inptDate)]
    get_batch_result = queryRun(getBatchQuery, cursorBB)

    return get_batch_result


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


# def txtFile(inptDict):
#     updDict = json.dumps(inptDict)
#     with open(path, 'w') as f:
#         f.write("%s\n" % updDict)


print(batchDict)
# txtFile(finalJson)

