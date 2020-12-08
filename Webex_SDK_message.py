from webexteamssdk import WebexTeamsAPI, ApiError

access_token = 'Y2RlNDdhMGItMTk0MS00YTdlLWI0ZDAtMWJlYWU5MWZiZWQ1OTI4ZjVkZDUtYzc2_PF84_consumer'
api = WebexTeamsAPI(access_token=access_token)

#room_id = Y2lzY29zcGFyazovL3VzL1JPT00vOWE1YmFkOTAtMGNkYy0xMWViLWE4OGEtNzc5MzQ5NGFmNzY3
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vMDIwYjc0NjAtMjg3Mi0xMWViLTgzZWItNDM2OGUzMDE1YTMx"
message = "Testando Webex SDK"

try:
    message = api.messages.create(room_id, text=message)
    print("New message created, with ID:", message.id)
    print(message.text)
except ApiError as e:
    print(e)