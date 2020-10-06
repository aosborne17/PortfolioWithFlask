from flask import Flask, render_template, redirect, url_for, request, session, flash, g
# from functools import wraps
import csv
from boto3.session import Session
import boto3
import os

PORT=5000

app = Flask(__name__)


@app.route("/")
def home():

    # whenever I enter my homepage I want to upload my CV to AWS

    ACCESS_KEY = os.environ["AWS_ACCESS_KEY"]
    SECRET_KEY = os.environ["AWS_SECRET_KEY"]

    s3_client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

    s3_client.upload_file('documents/CurriculumvitaeofAndrewOsborneOnePage.docx', 'andrew-mvc-with-itjobs', 'CurriculumvitaeofAndrewOsborneOnePage.docx')
    # now we can use the specific logger instead of root
    print("Your file has been successfully uploaded to an AWS bucket!")

    return render_template("index.html")


@app.route("/portfolio-item")
def portfolio_item():
    return render_template("portfolio-item.html")

@app.route("/run")
def run():
    print("Clicked")

    s3_client = boto3.client(
        's3',
        aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
        aws_secret_access_key=os.environ["AWS_SECRET_KEY"]
    )

    s3_client.download_file('andrew-mvc-with-itjobs', 'CurriculumvitaeofAndrewOsborneOnePage.docx',
                            '~/Downloads/CurriculumvitaeofAndrewOsborneOnePage.docx')

    return "Nothing"






# @app.route("/data", methods=['GET'])
# def data():
#     with open('ItJobsWatchTop30.csv', errors='ignore') as csv_file:
#         data = csv.reader(csv_file, delimiter=',')
#         jobs = []
#         no1job = []
#         no2job = []
#         no3job = []
#         counter = 1
#         for row in data:
#             # Skip the headers in the CSV file
#             if counter == 1:
#                 counter += 1
#                 continue
#             # Prepare 1st, 2nd and 3rd top results
#             elif counter == 2:
#                 no1job.append({
#                     "role": row[0],
#                     "rank": row[1],
#                     "rank_move": row[2],
#                     "median_salary": row[3],
#                     "median_percentage:": row[4],
#                     "hist_ads": row[5],
#                     "live_ads": row[6],
#                 })
#                 counter += 1
#                 continue
#             elif counter == 3:
#                 no2job.append({
#                     "role": row[0],
#                     "rank": row[1],
#                     "rank_move": row[2],
#                     "median_salary": row[3],
#                     "median_percentage:": row[4],
#                     "hist_ads": row[5],
#                     "live_ads": row[6],
#                 })
#                 counter += 1
#                 continue
#             elif counter == 4:
#                 no3job.append({
#                     "role": row[0],
#                     "rank": row[1],
#                     "rank_move": row[2],
#                     "median_salary": row[3],
#                     "median_percentage:": row[4],
#                     "hist_ads": row[5],
#                     "live_ads": row[6],
#                 })
#                 counter += 1
#                 continue

#             jobs.append({
#                 "role": row[0],
#                 "rank": row[1],
#                 "rank_move": row[2],
#                 "median_salary": row[3],
#                 "median_percentage:": row[4],
#                 "hist_ads": row[5],
#                 "live_ads": row[6],
#             })

#     return render_template("datapage.html",
#                            jobs=jobs, jobs1=no1job, jobs2=no2job, jobs3=no3job)


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly (so this will only respond to the 404 error)
    return render_template("404page.html"), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=PORT)