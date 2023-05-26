from queries.Pyro import *
from utils.FunctionUtils import *


def pyroService():
    print("PYRO Service Starts")
    # list of queries to get data for mail
    queriesListPyro = [classificationDetails,
                       extractionDetails, totalCount, splitCount]
    # mysql cursor for executing query
    # calling queryRun method in common function to execute and fetching results to resultListPyro
    resultListPyro = processQuery(queriesListPyro, "PYRO")
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
    print('PYRO Service Ends')
    return pyroHITLResult
