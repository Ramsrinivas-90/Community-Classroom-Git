classificationDetails = '''select WRKFLW_STEP,WRKFLW_STS,count(1) from (select I.ICE_ID, STEP.LKP_CD_DESC as WRKFLW_STEP, STS.LKP_CD_DESC as WRKFLW_STS, W.CURR_IND as CURR_IND 
from ICEe.WRKFLW_DTL W left join INGS_BLOB_DTL I on W.BLOB_DTL_ID = I.BLOB_DTL_ID
left join (select LKP_CD,LKP_CD_DESC from ICEe.VW_LKP_MAST_VAL where LKP_MAST_NM = 'WRKFLW_STEP_TYPE') STEP on W.WRKFLW_STEP_TYPE_ID =  cast(STEP.LKP_CD as UNSIGNED INTEGER)
left join (select LKP_CD,LKP_CD_DESC from ICEe.VW_LKP_MAST_VAL where LKP_MAST_NM = 'WRKFLW_STS_TYPE') STS on W.WRKFLW_STS_TYPE_ID =  cast(STS.LKP_CD as UNSIGNED INTEGER)
where W.CURR_IND = '1' AND W.CRE_DTTM >= NOW() - INTERVAL 24 HOUR  and (STEP.LKP_CD_DESC="HITL" or STEP.LKP_CD_DESC="Data Delivered")  and (STS.LKP_CD_DESC="Success Notified" or STS.LKP_CD_DESC="Queued") AND I.CLIENT_TYPE_ID = 4) A group by WRKFLW_STEP,WRKFLW_STS;;
'''
extractionDetails = '''select WRKFLW_STEP,WRKFLW_STS,count(1) from (select I.ICE_ID, STEP.LKP_CD_DESC as WRKFLW_STEP, STS.LKP_CD_DESC as WRKFLW_STS, W.CURR_IND as CURR_IND 
from ICEe.EDA_EXTRCTN_WRKFLW_DTL W left join INGS_BLOB_DTL I on W.BLOB_DTL_ID = I.BLOB_DTL_ID
left join (select LKP_CD,LKP_CD_DESC from ICEe.VW_LKP_MAST_VAL where LKP_MAST_NM = 'WRKFLW_STEP_TYPE') STEP on W.WRKFLW_STEP_TYPE_ID =  cast(STEP.LKP_CD as UNSIGNED INTEGER)
left join (select LKP_CD,LKP_CD_DESC from ICEe.VW_LKP_MAST_VAL where LKP_MAST_NM = 'WRKFLW_STS_TYPE') STS on W.WRKFLW_STS_TYPE_ID =  cast(STS.LKP_CD as UNSIGNED INTEGER)
where W.CURR_IND = '1' AND W.CRE_DTTM >= NOW() - INTERVAL 24 HOUR  and (STEP.LKP_CD_DESC="HITL" or STEP.LKP_CD_DESC="Data Delivered")  and (STS.LKP_CD_DESC="Success Notified" or STS.LKP_CD_DESC="Queued") AND I.CLIENT_TYPE_ID =4) A group by WRKFLW_STEP,WRKFLW_STS;'''

totalCount = '''select count(1) 
from WRKFLW_DTL W left join INGS_BLOB_DTL I on W.BLOB_DTL_ID = I.BLOB_DTL_ID	
where W.CURR_IND = '1' AND W.CRE_DTTM >= NOW() - INTERVAL 24 HOUR AND I.CLIENT_TYPE_ID = 4;'''

splitCount = '''SELECT DOC_TYPE,Count(DOC_TYPE) FROM ICEe.EDA_EXTRCTN_WRKFLW_DTL where BLOB_DTL_ID in (select I.BLOB_DTL_ID
from ICEe.EDA_EXTRCTN_WRKFLW_DTL W left join INGS_BLOB_DTL I on W.BLOB_DTL_ID = I.BLOB_DTL_ID
where W.CURR_IND = '1' AND W.CRE_DTTM >= NOW() - INTERVAL 24 HOUR AND WRKFLW_STS_TYPE_ID = '11' AND I.CLIENT_TYPE_ID = 4) and CURR_IND = '1' AND CRE_DTTM >= NOW() - INTERVAL 24 HOUR group by DOC_TYPE;'''
