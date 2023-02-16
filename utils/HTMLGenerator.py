from services.PyroService import pyroHITLResult
from services.BVService import BVHITLResult
from services.FlowService import flowFinalResults

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
        {BVHITLResult}
    <br>
        {pyroHITLResult}
    <br>
        {flowFinalResults}
    </body>
</html>  
'''
mailAttachment = f""" 
    {BVHITLResult}
    {pyroHITLResult}
    {flowFinalResults}
"""

with open("body.txt", "w") as file:
    file.write(mailAttachment)

print(HTMLBody)
