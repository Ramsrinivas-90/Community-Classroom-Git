import time
from concurrent.futures import ThreadPoolExecutor
from email.mime.multipart import MIMEMultipart

from future.backports.email.mime.text import MIMEText

from services.BBService import bbService, BBExtractionService
from services.PyroService import pyroService
from services.BVService import bvService
from services.FlowService import flowService

resultList = []
start = time.perf_counter()

taskList = [bvService, pyroService, flowService, BBExtractionService, bbService]

with ThreadPoolExecutor(100) as executor:
    running_tasks = [executor.submit(task) for task in taskList]
    for running_task in running_tasks:
        resultList.append(running_task.result())

style = '''
table {
    border-collapse: collapse;
    width: match-content;
    }
    td,
    th {
    border: 1px solid black;
    text-align: left;
    padding: 5px;
    width: match-content;
    text-align: center;
    }
    tr:nth-child(even) {
    background-color: #f2f2f2;
    }
    body {
    font-family: Arial;
    }
'''

msg = MIMEMultipart()
msg.preamble = 'PYRO Production Status'
# Attach HTML body
msg.attach(MIMEText(
    f'''
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title></title>
<style>
        {style}
        </style>
</head>
  <body style="margin: 0px; padding: 0px; background-color:#004261; background-position: top center;">
  <!-- BODY FAKE PANEL -->
        <!-- CENTER FLOAT -->
          <table width="1200" valign="top" align="center" bgcolor="#FFFFFF">
            <tr>
              <td align="center">
    <div style="text-align:left;margin:20px 30px;">
      Hi Team,
      <br />
      <br />
      PFB the updates from respective pods.
      <br />
        {resultList[0]}
        
        {resultList[1]}
        
        {resultList[2]}
        
        {resultList[4]}
        
        {resultList[3]}
        <br/>
        <div  style="color:#8fa1a6;font-weight:bold;font-family:SF UI Display;">
        Regards,
        <div style="color:#5F99F1;font-weight:bold;font-size:16px;font-family:SF UI Display">
        Status Mailer</div>
        </div>
         </td>
            </tr>
          </table>
        <!-- /CENTER FLOAT -->
  <!-- /BODY FAKE PANEL -->
  </body>
</html> 
''',
    'html', 'utf-8'))

end = time.perf_counter()
print(f'elapsed {end - start:0.2f} seconds')
print("Generated HTML Content")
