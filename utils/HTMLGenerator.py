from services.BBService import *
from services.PyroService import pyroHITLResult
from services.BVService import BVHITLResult
from services.FlowService import flowFinalResults

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

# show throughput if greater than 1000
throughputBody = ""
if throughput > 1000:
    throughputBody += """"<h4> NOTE: </h4>
    <ul>
        <li>
    <p> BB Throughput in last 24 hour - {throughput}  PagesPerMin </p>
        </li>
    </ul>"""

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
        {BVHITLResult}
        <br>
        {pyroHITLResult}
        <br>
        {flowFinalResults}
      <h3>Blob Buster:</h3>
      <p>{blobBusterUpdate}</p>
      <table>
        <tr>
          <th>Count/Type</th>
          <th>Classification</th>
          <th>Extraction</th>
        </tr>
        <tr>
          <td>Blob Count</td>
          <td>{dictBB['CLASSIFICATIONBLOBS']}</td>
          <td>{dictBB['EXTRACTIONBLOBS']}</td>
        </tr>
        <tr>
          <td>Page Count</td>
          <td>{int(dictBB['CLASSIFICATIONPAGES'])}</td>
          <td>{int(dictBB['EXTRACTIONPAGES'])}</td>
        </tr>
      </table>
      {throughputBody}
      <h3>MAG Update:</h3>
      <table>
        <tr>
          <th>Doc Type</th>
          <th>Count</th>
        </tr>
        {magTable}
      </table>
      <br />
    </body>
  </html>
</html>
"""

print('Mail-body Done')
