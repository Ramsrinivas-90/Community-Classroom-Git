from concurrent.futures import ThreadPoolExecutor
from utils.Env import *
import mysql.connector


# connecting to DB when required
def DBConnect(user, password, port):
    ICEe = mysql.connector.connect(
        host="127.0.0.1",
        user=user,
        password=password,
        database="ICEe",
        port=port
    )
    print("DB connected successfully")
    return ICEe


def processQuery(queryList, cursor):
    resultList = []
    with ThreadPoolExecutor(100) as executor:
        running_tasks = [executor.submit(executeQuery, query, cursor) for query in queryList]
        for running_task in running_tasks:
            resultList.append(running_task.result())
    return resultList


def executeQuery(query, useCase) -> list:
    ICEe = ""
    if useCase == "BV":
        ICEe = DBConnect(BVDBUserName,BVDBPassword,BVDBPort)
    elif useCase == "PYRO":
        ICEe = DBConnect(PYRODBUserName, PYRODBPassword, PYRODBPort)
    cursor = ICEe.cursor()
    cursor.execute(query)
    count = cursor.fetchall()
    ICEe.close()
    return count


# function to execute queries and fetching results
def queryRun(queryList, cursor):
    resultList = []
    for i in range(len(queryList)):
        cursor.execute(queryList[i])
        count = cursor.fetchall()
        resultList.append(count)
    return resultList


def extractionDocTable(splitCount, useCase):
    splitCountTable = ''

    # initializing loop length
    loopLength = len(splitCount)
    if loopLength == 0:
        return ''
    sentence = ''
    if useCase == 'FLOW' or useCase == 'Servicing':
        sentence = 'completed'
    else:
        sentence = 'HITL Success Notified'
    # formatting split count table of ext for HTML
    for i in range(0, loopLength):
        splitCountTable += '<tr>' + \
                           '<td>' + splitCount[i][0] + '</td>' + \
                           '<td>' + str(splitCount[i][1]) + '</td>' + \
                           '</tr>'
    extCountTable = f'''
        <br>
        <div> Below is the split up of documents for extraction {sentence}, </div>
        <table>
            <tr>
                <th> DocType </th>
                <th> Count </th>
            </tr>
        <div> {splitCountTable}</div>
        </table>
        '''
    return extCountTable


# Generating HTML based String for mail body
def formatter(classificationHITL, extractionHITL, useCase, totalCount, splitCount):
    HITLModifyTable = ''
    HITLTableList = [classificationHITL, extractionHITL]
    HITLResultList = []
    for j in range(len(HITLTableList)):
        for i in range(len(HITLTableList[j])):
            if len(HITLTableList[j]) == 1:
                HITLModifyTable += '<td>0</td><td>' + \
                                   str(HITLTableList[j][i][2]) + '</td>'
            else:
                HITLModifyTable += '<td>' + \
                                   str(HITLTableList[j][i][2]) + '</td>'
        HITLResultList.append(HITLModifyTable)
        HITLModifyTable = ''
    splitCountTable = extractionDocTable(splitCount, useCase)
    HITLTable = f'''
        <h3>{useCase}:</h3><div>Total Docs uploaded in last 24 hours - {totalCount} </div>
        <table>
            <tr>
                <th>Type/HITL Status</th>
                <th>HITL Queued</th>
                <th>HITL Success</th>
            </tr>
            <tr>
                <th>Classification</th>
                {HITLResultList[0]}     
            </tr>
            <tr>
                <th>Extraction</th>
                {HITLResultList[1]}
            </tr>
       </table> 
            {splitCountTable}
    '''

    if totalCount == 0:
        return f"""<h3> {useCase}: </h3> <div>No Docs uploaded in last 24 hours </div>"""
    return HITLTable
