classificationQuery = """SELECT
    COUNT(*) AS CNT,
    SUM(b.tot_pages) AS pages,
    SUM(b.tot_pages) / TIMESTAMPDIFF(MINUTE,
        NOW() - INTERVAL 24 HOUR,
        NOW()) AS PagePerMin
FROM
    ICEe.WRKFLW_DTL a
        JOIN
    ICEe.INGS_BLOB_DTL b ON a.BLOB_DTL_ID = b.BLOB_DTL_ID
WHERE
    a.CRE_DTTM >= NOW() - INTERVAL 24 HOUR
        AND a.CRE_DTTM <= NOW()
        AND a.WRKFLW_STEP_TYPE_ID = 5
        AND a.WRKFLW_STS_TYPE_ID = 2
        AND (a.QUEUE_TYPE_ID > 1 AND a.QUEUE_TYPE_ID < 7
        OR (a.QUEUE_TYPE_ID > 37))
GROUP BY a.WRKFLW_STEP_TYPE_ID , a.WRKFLW_STS_TYPE_ID;"""

extractionQuery = """SELECT 
    COUNT(*) AS CNT,
    SUM(pg_cnt.PAGE_COUNT) AS pages
FROM
    ICEe.EDA_EXTRCTN_WRKFLW_DTL a
        JOIN
    ICEe.INGS_BLOB_DTL b ON a.BLOB_DTL_ID = b.BLOB_DTL_ID
        JOIN
    (SELECT 
        cp.BLOB_DTL_ID, COUNT(1) AS PAGE_COUNT
    FROM
        CLS_PAGE_CLUSTER_DTL cp
    JOIN CLS_CLUSTER_DTL cc ON cc.CLUSTER_DTL_ID = cp.CLUSTER_DTL_ID
    JOIN ICEe.VW_LKP_MAST_VAL ct ON ct.LKP_MAST_NM = 'CLUSTER_TYPE'
        AND cc.CLUSTER_TYPE_ID = ct.LKP_CD
        AND EXTRCTN_FLAG = 'Y'
    WHERE
        cp.BLOB_DTL_ID IN (SELECT 
                BLOB_DTL_ID
            FROM
                EDA_EXTRCTN_WRKFLW_DTL
            WHERE
                CRE_DTTM > NOW() - INTERVAL 24 HOUR)
    GROUP BY cp.BLOB_DTL_ID) pg_cnt ON pg_cnt.BLOB_DTL_ID = a.BLOB_DTL_ID
WHERE
    a.CRE_DTTM >= NOW() - INTERVAL 24 HOUR
        AND a.WRKFLW_STEP_TYPE_ID = 11
        AND a.WRKFLW_STS_TYPE_ID = 2
        AND (a.QUEUE_TYPE_ID > 1 AND a.QUEUE_TYPE_ID < 7
        OR (a.QUEUE_TYPE_ID > 37))
GROUP BY a.WRKFLW_STEP_TYPE_ID , a.WRKFLW_STS_TYPE_ID;"""

ingestionBlobs = '''SELECT Batch_ID,count(1) from ICE_Ingestion.ICEIngestion where Status is NULL group by Batch_ID;'''

bbExtractionSplitCountQuery = '''Select DOC_TYPE,count(1) as COUNT from (select W.DOC_TYPE
from EDA_EXTRCTN_WRKFLW_DTL W
where
W.CURR_IND = 1 AND 
W.WRKFLW_STEP_TYPE_ID = 11 AND
W.WRKFLW_STS_TYPE_ID = 2 AND
 (W.QUEUE_TYPE_ID > 1 AND W.QUEUE_TYPE_ID < 7
        OR (W.QUEUE_TYPE_ID > 37)) AND
W.CRE_DTTM >= NOW() - INTERVAL 24 HOUR)B group by DOC_TYPE;'''