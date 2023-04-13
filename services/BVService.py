from queries.BV import *
from utils.FunctionUtils import *
from utils.Env import BVDBUserName, BVDBPassword, BVDBPort


def bvService():
    print("Bayview Service Starts")
    ICEe = DBConnect(BVDBUserName,BVDBPassword, BVDBPort)
    # resultList of queries to get data for mail
    queriesListBV = [classificationDetailsBV,
                     extractionDetailsBV, totalCountBV, splitCountBV]
    # mysql cursor for executing query
    cursorBV = ICEe.cursor()
    # calling queryRun method in common function to execute and fetching results to resultListPyro
    resultListBV = processQuery(queriesListBV, cursorBV)
    ICEe.close()
    # fetching classification HITL counts both queued and success notified
    classificationHITLBV = resultListBV[0]
    # fetching extraction HITL counts both queued and success notified
    extractionHITLBV = resultListBV[1]
    # fetching total number of docs uploaded
    totalDocBV = resultListBV[2][0][0]
    # fetching split count of extraction with doc types
    splitCountExtrctnBV = resultListBV[3]
    # calling formatter method from commonFunction to get HTML Format of cls and ext HITL Table
    BVHITLResult = formatter(classificationHITLBV,
                             extractionHITLBV, "Bayview", totalDocBV, splitCountExtrctnBV)
    print("Bayview Service Ends")
    return BVHITLResult


