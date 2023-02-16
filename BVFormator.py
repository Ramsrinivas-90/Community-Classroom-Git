from MailQueries import *
from CommonFunction import *
from env import BVDBPassword, BVDBUserName
ICEe = DBConnect(BVDBUserName, BVDBPassword, "3300")


# list of queries to get data for mail
queriesListBV = [classificationDetails,
                 extractionDetails, totalCount, splitCount]
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

# fetching split count of extraction with doc types
splitCountExtrctnBV = resultListBV[3]

# calling formatter method from commonFunction to get HTML Format of cls and ext HITL Table
BVHITLResult = formatter(classificationHITLBV,
                         extractionHITLBV, "Bayview", totalDocBV, splitCountExtrctnBV)
