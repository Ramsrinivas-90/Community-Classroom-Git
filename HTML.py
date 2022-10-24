from PyroFormator import *
from BVFormator import *

style = """
table
    { border-collapse:collapse; width:match-content;}
td, th
    {border: 1px solid black; text-align: left; padding: 5px;, width:match-content; text-align: center;}
tr:nth-child(even) {background-color: #f2f2f2;}
body{
    font-family: apple-system, BlinkMacSystemFont, sans-serif;
color:#2f55a4}
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
        {pyroHITLResult}
    <br>
    <p>Below is the split up of documents for extraction HITL Success Notified,</p>
    <table>
        <tr>
            <th>DocType</th>
            <th>Count</th>
        </tr>
        <p>{splitCountTable}</p>
    </table>
    </body>
</html>  
'''
mailAttachment = f""" {BVHITLResult}
        {pyroHITLResult}
    <br>
    <p>Below is the split up of documents for extraction HITL Success Notified,</p>
    <table>
        <tr>
            <th>DocType</th>
            <th>Count</th>
        </tr>
        <p>{splitCountTable}</p>
    </table>"""

with open("body.txt", "w") as file:
    file.write(mailAttachment)
