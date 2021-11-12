# Python tkinter hello world program
  
import tkinter as tk
# import requests
# import json

# Before you run this python script:

# 1. Replace YOUR_CLIENT_ID with your client_id.
# 2. Replace YOUR_CLIENT_SECRET with your client_secret.
# 3. Ensure the URL is correct for your instance.
#    For the OAuth call to get an access_token, the url should be SERVERNAME.degreed.com
#    For the API calls that follow, the url should be api.SERVERNAME.degreed.com
# 4. In the data section toward the bottom, replace employee-id and organization-email with new, unique values.
# 5. Run the python script.

# ----- Get Access Token ----- */

# url = "https://betatest.degreed.com/oauth/token"

# payload = "scope=users%3Aread%20users%3Awrite%20user_skills%3Awrite" + "&" + \
# "grant_type=client_credentials" + "&" + \
# "client_id=YOUR_CLIENT_ID" + "&" + \
# "client_secret=YOUR_CLIENT_SECRET"
# headers = {
#     "Content-Type": "application/x-www-form-urlencoded"
# }

# # make the request to get an access_token
# response = requests.request("POST", url, data=payload, headers=headers)

# # extract the request into a json object
# responsedata = json.loads(response.text)
# access_token = responsedata["access_token"]



# # ----- Use Access Token to Request GET ALL users-----*/

# url = "https://api.betatest.degreed.com/api/v2/users"

# payload = ""
# headers = {
#     "Authorization": "Bearer " + access_token
# }

# # make the request to GET all users
# response = requests.request("GET", url, data=payload, headers=headers)

# # print response body from request
# print("List of all users:")
# print(response.text)



# # ----- Wait for ENTER Key -----

# pause = input("Press enter to continue")



# # # ----- Use Access Token to Make Request CREATE user -----*/
# # #
# # # NOTE: You must change employee-id and email before running. These values must must be unique.
# # # You can also change other values.

# # url = "https://api.betatest.degreed.com/api/v2/users"

# # data = {
# #     "data": {
# #         "type": "users",
# #         "attributes": {
# #             "employee-id": "62342",
# #             "first-name": "Bob",
# #             "last-name": "Hope",
# #             "full-name": "Bob Hope",
# #             "organization-email": "bobhope@shazam.com",
# #             "profile-visibility": "Organization",
# #             "bio": "ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent blandit nam",
# #             "location": "Naha-shi",
# #             "profile-image-url": "",
# #             "login-disabled": "true",
# #             "restricted": "true",
# #             "permission-role": "Member",
# #             "real-time-email-notification": "true",
# #             "daily-digest-email": "true",
# #             "weekly-digest-email": "false"
# #         }
# #     }
# # }

# payload = json.dumps(data)

# headers = {
#     "Authorization": "Bearer " + access_token
# }

# # make the request to POST a user
# response = requests.request("POST", url, data=payload, headers=headers)


  
master = tk.Tk()
tk.Label(master, text ="Please enter your name below").grid(row=0)
tk.Label(master, text="First Name").grid(row=1)
tk.Label(master, text="Last Name").grid(row=2)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
  
master.mainloop()
