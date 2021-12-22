# Python tkinter hello world program
  
import tkinter as tk
from tkinter import ttk
import requests
import json
import xml.etree.ElementTree as ET

# Before you run this python script:

# 1. Replace YOUR_CLIENT_ID with your client_id.
# 2. Replace YOUR_CLIENT_SECRET with your client_secret.
# 3. Ensure the URL is correct for your instance.
#    For the OAuth call to get an access_token, the url should be SERVERNAME.degreed.com
#    For the API calls that follow, the url should be api.SERVERNAME.degreed.com
# 4. In the data section toward the bottom, replace employee-id and organization-email with new, unique values.
# 5. Run the python script.

# ----- Get Access Token ----- */

def main():
    buildtkinter()

def userflow(ourinput, inputtype):
    endpoint = build_url(inputtype, ourinput)
    get_user_call(endpoint)

def open_popup(msg):
    popup = tk.Tk()
    popup.wm_title("User Data Results")
    label = ttk.Label(popup, text=msg)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def buildtkinter():
    def search_email():
        userflow(str(e1.get()).strip(), "email")
    def search_ID():
        userflow(str(e1.get()).strip(), "ID")

    master = tk.Tk()
    master.title("Degreed API APP")
    tk.Label(master, text="Please enter your user ID for the user you are looking for").grid(row=0)
    tk.Label(master).grid(row=1)
    
    e1 = tk.Entry(master)
    e1.grid(row=1, column=0) 

    f1 = tk.Frame(master)

    b1 = tk.Button(f1, text='Search Email', command=search_email)
    b2 = tk.Button(f1, text='Search ID', command=search_ID)
    b3 = tk.Button(f1, text='Quit', command=master.quit)

    f1.grid(row=2, column=0, sticky="nsew")

    b1.pack(side="top")
    b2.pack(side="top")
    b3.pack(side="top")

    tk.mainloop()

def build_url(urltype, useridentifer):
    url = "No URL"
    if urltype == "email":
        url = 'https://api.betatest.degreed.com/api/v2/users/'+useridentifer+'?identifier=email'
    if urltype == "ID":
        url = "https://api.betatest.degreed.com/api/v2/users/" + useridentifer + "?identifier=employee-id"
    return url

def get_user_call(endpoint):
    url = "https://betatest.degreed.com/oauth/token"

    payload = "scope=users%3Aread%20users%3Awrite%20user_skills%3Awrite" + "&" + \
    "grant_type=client_credentials" + "&" + \
    "client_id=590075deea8fb914" + "&" + \
    "client_secret=786bb7a33f2c0f47aa3e7937714d754d"
    headers = {
    "Content-Type": "application/x-www-form-urlencoded"
    }

    # make the request to get an access_token
    response = requests.request("POST", url, data=payload, headers=headers)

    # extract the request into a json object
    responsedata = json.loads(response.text)
    access_token = responsedata["access_token"]

    payload = ""
    headers = {
    "Authorization": "Bearer " + access_token
    }

    # make the request to GET all users
    # use the endpoint in the request we sent in as a parameter
    response = requests.request("GET", endpoint, data=payload, headers=headers)
    jsonResponse =  json.loads(response.text)

    
    exportstring = ""
    for datapoints in jsonResponse:
        exportstring += "-------------\n"
        exportstring += "User ID -> " + jsonResponse["data"]["id"] + "\n"
        for moredatapoints in jsonResponse[datapoints]["attributes"]:
            exportstring += moredatapoints + "->" + str(jsonResponse[datapoints]["attributes"][moredatapoints]) + "\n"
        for moredatapoints in jsonResponse[datapoints]["links"]:
            exportstring += moredatapoints + '->' + str(jsonResponse[datapoints]["links"][moredatapoints]) + "\n"
        exportstring += "-------------"
    open_popup(exportstring)

main()
        








    
