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

taskList = [bvService,pyroService,flowService,BBExtractionService,bbService]

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
    font-family: apple-system, BlinkMacSystemFont, sans-serif;
    color: #2f55a4;
    }
'''

msg = MIMEMultipart()
msg.preamble = 'Status On Production Blobs'
# Attach HTML body
msg.attach(MIMEText(
    f'''
    <html>
    <head>
        <style>
        {style}
        </style>
    </head>
    <body>
      Hi Team,
      <br />
      <br />
      PFB the updates from respective pods.
      <br />
        {resultList[0]}
        <br>
        {resultList[1]}
        <br/>
        {resultList[2]}
        {resultList[4]}
        <br/>
        {resultList[3]}
    </body>
</html>  
''',
    'html', 'utf-8'))

end = time.perf_counter()
print(f'elapsed {end - start:0.2f} seconds')
print("Generated HTML Content")


