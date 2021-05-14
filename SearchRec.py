# Python script that reads data from a CSV File 
# Inserts them into a mail template
# Despatches mail via sendgrid API

import csv
import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, Content)


data = []
with open("<File_Name>") as csvf: # Insert the name of the csv file with path specified
    readfile = csv.reader(csvf)
    for row in readfile:
        data.append(row)



name = input("Enter full name: ")

col = [x[1] for x in data]


if name in col:
    print("Employee found in list");
    purpose = input("Enter purpose: ")
    for x in range(1,len(data)):
        if name == data[x][1]:
            address = data[x][2]
            tenure = data[x][3]
            designation = data[x][4]
            emp_manager = data[x][5]
            recv_email = data[x][6]
            leave_bal = data[x][7]

print(''' Details: \nName:''', name,
      '''\nAddress:''', address,
      '''\nTenure:''',tenure,
      '''\nDesignation:''',designation,
      '''\nManager's Name:''',emp_manager,
      '''\nManager's email:''',recv_email,
      '''\nLeave Balance:''',leave_bal)


message = """
            // <html content>
          """
                


message = Mail(
    from_email='<Sender\'s mail>',
    to_emails=recv_email,
    subject='<Subject line>',
    html_content= message.format(purpose=purpose,name=name,address=address,tenure=tenure,designation=designation)
)

mail_json = message.get()

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.client.mail.send.post(request_body=mail_json)

print(response.status_code, response.body, response.headers)

