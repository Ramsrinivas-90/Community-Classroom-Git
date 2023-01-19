from MailQueriesFlow import *
from CommonFunction import *
from env import PYRODBPassword, PYRODBUserName
ICEe = DBConnect(PYRODBUserName, PYRODBPassword, "3300")

# list of queries to get data for mail
queriesListFLOW = [flowQuery,
                   flowCompleted, flowDocs, flowExtractionDocCount]
# mysql cursor for executing query
cursor = ICEe.cursor()

# calling queryRun method in common function to execute and fetching results to resultListPyro
resultFlow = queryRun(queriesListFLOW, cursor)

flowClassification = resultFlow[0]
flowClsCompleted = resultFlow[1]
flowSellers = resultFlow[2]
flowExtCompleted = resultFlow[3]
totalCount = 0
completed = 0
fileValidationFailed = 0
loanValidationFailed = 0

if flowSellers and flowClsCompleted and flowClassification:
    for i in range(len(flowClassification)):
        if flowClassification[i][0] == "Loan Validation":
            loanValidationFailed = flowClassification[i][2]
        elif flowClassification[i][0] == "File Validation":
            fileValidationFailed = flowClassification[i][2]
        totalCount += flowClassification[i][2]
    completed = flowClsCompleted[0][2]
    flowSellerDetails = ''

    batchLoop = len(flowSellers)
    for i in range(0, batchLoop):
        flowSellerDetails += '<tr>' + \
                             '<td>' + flowSellers[i][0] + '</td>' + \
                             '<td>' + flowSellers[i][1] + '</td>' + \
                             '<td>' + str(flowSellers[i][2]) + '</td>' + \
                             '</tr>'
    extDocTable = extractionDocTable(flowExtCompleted, 'FLOW')
    flowFinalResults = f"""<h4>Flow:</h4>
        <table id="flow">
        <tr>
            <th>Total Docs</th>
            <th>Completed </th>
            <th>Loan Validation Failed</th>
            <th>File Validation Failed</th>
        </tr>
        <tr>
            <td>{totalCount}</td>
            <td>{completed}</td>
            <td>{loanValidationFailed}</td>
            <td>{fileValidationFailed}</td>
        </tr>
        </table>
        <br>
        <br>
        <table id="seller">
        <tr>
            <th>Seller</th>
            <th>FileType</th>
            <th>Count</th>
        </tr>
        {flowSellerDetails}
        </table>
        <br>
        {extDocTable}
        """
else:
    flowFinalResults = """<h4>Flow:</h4>
        <p>No Docs were uploaded in last 24 hours.</p>"""
