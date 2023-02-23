import time

from services.PyroService import pyroService
from services.BVService import bvService
from services.FlowService import flowService
from concurrent.futures import ThreadPoolExecutor

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
    lambda: flowService()
])

style = """
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
"""

HTMLBody = f'''
    <html>
    <head>
        <style>
        {style}
        </style>
    </head>
    <body>
        {resultList[0]}
    <br>
        {resultList[1]}
    <br>
        {resultList[2]}
    </body>
</html>  
'''
mailAttachment = f""" 
    {resultList[0]}
    {resultList[1]}
    {resultList[2]}
"""

with open("body.txt", "w") as file:
    file.write(mailAttachment)
end = time.perf_counter()
print(f'elapsed {end - start:0.2f} seconds')
print("Generated HTML Content")
