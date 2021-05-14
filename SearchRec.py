import csv
import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import (Mail, Attachment, Content)
data = []
with open("Emp_Record.csv") as csvf:
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


message = """Dear Sir,
             <br>Request for  bonafide certificate for the purpose of <b>{purpose}</b>
             <br>Details of employee are as follows:                    
             <br>Name: {name}                     
             <br>Address: {address}
             <br>Tenure: {tenure}
             <br>Designation: {designation}
             <br>Kindly issue an attested copy of the bonafide certificate.
             
             """
                


message = Mail(
    from_email='hrxbot@gmail.com',
    to_emails=recv_email,
    subject='Request for Bonafide Certicate',
    html_content= message.format(purpose=purpose,name=name,address=address,tenure=tenure,designation=designation)
)
mail_json = message.get()

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
response = sg.client.mail.send.post(request_body=mail_json)

print(response.status_code, response.body, response.headers)

