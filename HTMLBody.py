from MailFormator import *
from HTML import HTMLBody

#
# with open("Signature.html", "r") as sign:
#     signature = sign.read()


style = """table,body{
font-family: apple-system, BlinkMacSystemFont, sans-serif;
border-collapse: collapse;
width: match-content;
color : #2f55a4;
}

td, th {
  border: 1px solid black;
  text-align: center;
  padding: 5px;
  width: match-content;
}

#flow{
    width: 600px;
}

#seller{
    width: 450px;
}

tr:nth-child(even) {
background-color: #f2f2f2;
}"""

powerBI = f"""  <h4>
                PowerBI Report:
                </h4>
                <table>
                    {tableHeaderHTML + tableContent + tableFooterHTML}
                </table>"""
throughputBody = ""
if throughput > 1000:
    throughputBody += """"<h4> NOTE: </h4>
    <ul>
        <li>
    <p> BB Throughput in last 24 hour - {throughput}  PagesPerMin </p>
        </li>
    </ul>"""
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
      {HTMLBody}
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
        <tr>
          <td>Note</td>
          <td>{dictMag['NOTE']}</td>
        </tr>
        <tr>
          <td>Mortgage</td>
          <td>{dictMag['MORTGAGE']}</td>
        </tr>
        <tr>
          <td>Appraisal</td>
          <td>{dictMag['APPRAISAL']}</td>
        </tr>
        <tr>
          <td>1003</td>
          <td>{dictMag['1003']}</td>
        </tr>
        <tr>
          <td>W9</td>
          <td>{dictMag['W9']}</td>
        </tr>
        <tr>
          <td>SSN</td>
          <td>{dictMag['SSN']}</td>
        </tr>
        <tr>
          <td>CD</td>
          <td>{dictMag['CD']}</td>
        </tr>
      </table>
      <br />
    </body>
  </html>
</html>
"""

print(htmlbody)
