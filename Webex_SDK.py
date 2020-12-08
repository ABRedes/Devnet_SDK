from webexteamssdk import WebexTeamsAPI, ApiError
access_token = 'Y2RlNDdhMGItMTk0MS00YTdlLWI0ZDAtMWJlYWU5MWZiZWQ1OTI4ZjVkZDUtYzc2_PF84_consumer'
api = WebexTeamsAPI(access_token=access_token)
try:
    me = api.people.me()
    print(f"\nEmail associado ao meu usuário: {me.emails}\n")

    rooms = api.rooms.list()
    for room in rooms:
        if "DEVASC" in room.title:
            print (room.id, room.title)
except ApiError as e:
    print(e)