from queries.BB import *
from utils.FunctionUtils import *
from datetime import date
from datetime import timedelta
from utils.Env import PYRODBUserName, PYRODBPassword, PYRODBPort
import json

yesterday = date.today() - timedelta(1)


def formatBatchDetails(batchDetails):
    if len(batchDetails) == 0:
        return "No batches were uploaded in last 24 hour."
    batchDetailsTable = '''
        <p>PFB batches uploaded in blob buster last 24 hour.</p> 
        <table>
        <tr>
          <th>Queue</th>
          <th>Batch</th>
          <th>Uploaded Date</th>
        </tr>'''
    for batchDetail in batchDetails:
        batchDetailsTable += f'<tr><td>{str(batchDetail[0])}</td>' \
                             f'<td>{str(batchDetail[1])}</td>' \
                             f'<td>{str(batchDetail[2])}</td></tr>'
    batchDetailsTable += '</table>'
    return batchDetailsTable


def get_batch(inptDate):
    getBatchQuery = ["""SELECT IQT.QUEUE_TYPE_DESC,SII.Batch_ID,DATE_FORMAT(SII.CRE_DTTM, '%Y-%m-%d')  FROM ICE_Ingestion.STG_ICEIngestion SII 
    join ICE_Ingestion.INGS_QUEUE_TYPE IQT on SII.QUEUE_TYPE_ID = IQT.QUEUE_TYPE_ID where  SII.CRE_DTTM like "%{}%" 
    order by SII.Batch_ID; """.format(
        inptDate)]
    get_batch_result = processQuery(getBatchQuery, "PYRO")[0]
    return formatBatchDetails(get_batch_result)


def bbService():
    print("Starting BB Service")
    batch = get_batch(yesterday)
    # batchList = []
    # for i in range(0, len(batch)):
    #     batchList.append(batch[i][0])
    # batchDict = {}
    # for i in range(0, len(batchList)):
    #     batchDict[batchList[i]] = []
    #     for j in range(0, len(batch)):
    #         if batch[j][0] == batchList[i]:
    #             batchDict[batchList[i]].append(batch[j][1])
    queriesListBB = [classificationQuery, extractionQuery]
    resultListBB = processQuery(queriesListBB, "PYRO")
    dictBB = {}
    bbClassificationDetails = ["CLASSIFICATIONBLOBS", "CLASSIFICATIONPAGES"]
    bbExtractionDetails = ["EXTRACTIONBLOBS", "EXTRACTIONPAGES"]
    blobBusterUpdate = ''
    # batchLoop = len(list(batchDict.keys()))
    # if batchLoop:
    #     for i in range(0, batchLoop):
    #         blobBusterUpdate += 'Batch ' + \
    #                             str(batchDict[list(batchDict.keys())[i]]) + ' in ' + \
    #                             list(batchDict.keys())[i] + ',\n'
    #     blobBusterUpdate = blobBusterUpdate.replace("[", "").replace("]", "") + "uploaded in last 24 hours."
    #
    # elif batchLoop == 0:
    #     blobBusterUpdate += "No batches were uploaded in last 24 hour."
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
    # show throughput if greater than 1000
    throughputBody = ""
    if throughput > 1000:
        throughputBody += f"""<h4> NOTE: </h4>
        <ul>
            <li>
        <p> BB Throughput in last 24 hour - {throughput}  PagesPerMin </p>
            </li>
        </ul>"""
    bbResult = f'''<h3>Blob Buster:</h3>
      <p>{batch}</p>
      <br/>
      <table>
        <tr>
          <th>Count/Type</th>
          <th>Classification</th>
          <th>Extraction</th>
        </tr>
        <tr>
          <td>Blob Count</td>
          <td>{dictBB['CLASSIFICATIONBLOBS']}</td>
          <td>{dictBB['EXTRACTIONBLOBS']}</td>
        </tr>
        <tr>
          <td>Page Count</td>
          <td>{int(dictBB['CLASSIFICATIONPAGES'])}</td>
          <td>{int(dictBB['EXTRACTIONPAGES'])}</td>
        </tr>
      </table>
      {throughputBody}'''
    print("BB Service Ends")
    return bbResult


def BBExtractionService():
    print("Starting BB Extraction Doc Split up Service")
    # queriesListMag = [magNOTE, magMortgage, magAppraisal, mag1003, magW9, magSSN, magCD]
    # resultListMag = processQuery(queriesListMag, cursorBB)
    # dictMag = {}
    # magDoc = ["NOTE", "MORTGAGE", "APPRAISAL", "1003",  "W9", "SSN", "CD"]
    # for i in range(7):
    #     if len(resultListMag[i]) == 0:
    #         dictMag[magDoc[i]] = 0
    #     else:
    #         dictMag[magDoc[i]] = resultListMag[i][0][2]
    #
    # magTable = ""
    # for i in range(0, len(magDoc)):
    #     magTable += '<tr>' + \
    #                 '<td>' + magDoc[i] + '</td>' + \
    #                 '<td>' + str(dictMag[magDoc[i]]) + '</td>' + \
    #                 '</tr>'
    # print('MAG Done')
    resultListEXTBB = processQuery([bbExtractionSplitCountQuery], "PYRO")
    BBExtTable = extractionDocTable(resultListEXTBB[0], "Servicing")
    print("BB Extraction Doc Split up Service Ends")
    return BBExtTable
