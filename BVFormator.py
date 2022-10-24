from re import I
from MailQueriesBV import *
from CommonFunction import *
from Secrets import BVDBPassword, BVDBUserName
ICEe = DBConnect(BVDBUserName, BVDBPassword, "3301")


# list of queries to get data for mail
queriesListBV = [classificationDetailsBV,
                 extractionDetailsBV, totalCountBV]
# mysql cursor for executing query
cursorBV = ICEe.cursor()

# calling queryRun method in common function to execute and fetching results to resultListPyro
resultListBV = queryRun(queriesListBV, cursorBV)

# fetching classification HITL counts both queued and success notified
classificationHITLBV = resultListBV[0]

# fetching extraction HITL counts both queued and success notified
extractionHITLBV = resultListBV[1]

# fetching total number of docs uploaded
totalDocBV = resultListBV[2][0][0]

# calling formatter method from commonFunction to get HTML Format of cls and ext HITL Table
BVHITLResult = formatter(classificationHITLBV,
                         extractionHITLBV, "Bayview", totalDocBV)
