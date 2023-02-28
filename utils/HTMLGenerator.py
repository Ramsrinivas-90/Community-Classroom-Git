from concurrent.futures import ThreadPoolExecutor

from services.BBService import bbService, magService
from services.PyroService import pyroService
from services.BVService import bvService
from services.FlowService import flowService

resultList = []
start = time.perf_counter()


def run_io_tasks_in_parallel(tasks):
    with ThreadPoolExecutor() as executor:
        running_tasks = [executor.submit(task) for task in tasks]
        for running_task in running_tasks:
            resultList.append(running_task.result())


run_io_tasks_in_parallel([
    lambda: bvService(),
    lambda: pyroService(),
    lambda: flowService(),
    lambda: magService(),
    lambda: bbService()
])

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

# html body declaration
htmlbody = f"""<html>
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
        <br>
        {resultList[2]}
        {resultList[4]}
      <h3>MAG Update:</h3>
      <table>
        <tr>
          <th>Doc Type</th>
          <th>Count</th>
        </tr>
        {resultList[3]}
      </table>
      <br />
    </body>
  </html>
</html>
"""
end = time.perf_counter()
print(f'elapsed {end - start:0.2f} seconds')
print("Generated HTML Content")
