from MailQueriesFlow import *
from CommonFunction import *
from env import PYRODBPassword, PYRODBUserName
ICEe = DBConnect(PYRODBUserName, PYRODBPassword, "3300")

# list of queries to get data for mail
queriesListFLOW = [flowQuery,
                   flowCompleted, flowDocs]
# mysql cursor for executing query
cursor = ICEe.cursor()

# calling queryRun method in common function to execute and fetching results to resultListPyro
resultFlow = queryRun(queriesListFLOW, cursor)

query1Results = resultFlow[0]
query2Results = resultFlow[1]
query3Results = resultFlow[2]
totalCount = 0
completed = 0
fileValidationFailed = 0
loanValidationFailed = 0

if query3Results and query2Results and query1Results:
    for i in range(len(query1Results)):
        if query1Results[i][0] == "Loan Validation":
            loanValidationFailed = query1Results[i][2]
        elif query1Results[i][0] == "File Validation":
            fileValidationFailed = query1Results[i][2]
        totalCount += query1Results[i][2]
    completed = query2Results[0][2]
    flowSellerDetails = ''

    batchLoop = len(query3Results)
    for i in range(0, batchLoop):
        flowSellerDetails += '<tr>' + \
                             '<td>' + query3Results[i][0] + '</td>' + \
                             '<td>' + query3Results[i][1] + '</td>' + \
                             '<td>' + str(query3Results[i][2]) + '</td>' + \
                             '</tr>'

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
        </table>"""
else:
    flowFinalResults = """<h4>Flow:</h4>
        <p>No Docs were uploaded in last 24 hours.</p>"""

print(flowFinalResults)
