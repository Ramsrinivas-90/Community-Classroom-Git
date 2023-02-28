from queries.Pyro import *
from utils.FunctionUtils import *
from utils.Env import PYRODBPassword, PYRODBUserName, PYRODBPort


def pyroService():
    ICEe = DBConnect(PYRODBUserName, PYRODBPassword, PYRODBPort)

    # list of queries to get data for mail
    queriesListPyro = [classificationDetails,
                       extractionDetails, totalCount, splitCount]

    # mysql cursor for executing query
    cursorPyro = ICEe.cursor()

    # calling queryRun method in common function to execute and fetching results to resultListPyro
    resultListPyro = processQuery(queriesListPyro, cursorPyro)

    # fetching classification HITL counts both queued and success notified
    classificationHITL = resultListPyro[0]

    # fetching extraction HITL counts both queued and success notified
    extractionHITL = resultListPyro[1]

    # fetching total number of docs uploaded
    totalDocPyro = resultListPyro[2][0][0]

    # fetching split count of extraction with doc types
    splitCountExtrctnPyro = resultListPyro[3]

    # calling formatter method from commonFunction to get HTML Format of cls and ext HITL Table
    pyroHITLResult = formatter(
        classificationHITL, extractionHITL, "Pyro V2 Originations", totalDocPyro, splitCountExtrctnPyro)
    print('Pyro Done')
    return pyroHITLResult

# # initializing empty string for formatting HTML for split count of ext
# splitCountTable = ''

# # initializing loop length
# batchLoop = len(splitCountExtrctnPyro)

# # formatting split count table of ext for HTML
# for i in range(0, batchLoop):
#     splitCountTable += '<tr>' + \
#         '<td>' + splitCountExtrctnPyro[i][0]+'</td>' + \
#         '<td>' + str(splitCountExtrctnPyro[i][1]) + '</td>' + \
#         '</tr>'
#     extractionSuccess += splitCountExtrctnPyro[i][1]
