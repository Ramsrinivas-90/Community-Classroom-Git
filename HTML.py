from PyroFormator import pyroHITLResult
from BVFormator import BVHITLResult
from FlowFormator import flowFinalResults

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

print(HTMLBody)
