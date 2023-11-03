#  _______  _        _______  _______  _          _______             _______  _______  _______  _______  _______  _______  _______  _______
# (  ____ \( \      (  ____ \(  ___  )( (    /|  (       )|\     /|  (       )(  ____ \(  ____ \(  ____ \(  ___  )(  ____ \(  ____ \(  ____ \
# | (    \/| (      | (    \/| (   ) ||  \  ( |  | () () |( \   / )  | () () || (    \/| (    \/| (    \/| (   ) || (    \/| (    \/| (    \/
# | |      | |      | (__    | (___) ||   \ | |  | || || | \ (_) /   | || || || (__    | (_____ | (_____ | (___) || |      | (__    | (_____
# | |      | |      |  __)   |  ___  || (\ \) |  | |(_)| |  \   /    | |(_)| ||  __)   (_____  )(_____  )|  ___  || | ____ |  __)   (_____  )
# | |      | |      | (      | (   ) || | \   |  | |   | |   ) (     | |   | || (            ) |      ) || (   ) || | \_  )| (            ) |
# | (____/\| (____/\| (____/\| )   ( || )  \  |  | )   ( |   | |     | )   ( || (____/\/\____) |/\____) || )   ( || (___) || (____/\/\____) |
# (_______/(_______/(_______/|/     \||/    )_)  |/     \|   \_/     |/     \|(_______/\_______)\_______)|/     \|(_______)(_______/\_______)
#
# DM & Message Cleaner written in python by TOXIC1835 <3

import requests

channel_id = 123  # channel id NOT user id
limit = 100  # let the last x messages load and try to delete

head = {
    "Authorization": "TOKEN"  # Your discord token (if bot "Bearer TOKEN")
}

r = requests.get(f"https://discord.com/api/v9/channels/{channel_id}/messages?limit={limit}", headers=head)

if r.status_code == 200:
    messages = r.json()

    msg_ids = [message["id"] for message in messages]

    for msg_id in msg_ids:
        delete_url = f"https://discord.com/api/v9/channels/{channel_id}/messages/{msg_id}"
        delete_response = requests.delete(delete_url, headers=head)

        if delete_response.status_code == 204:
            print(f"SUCCEED > delete  -> {msg_id}")
        else:
            print(f"ERROR   > delete  -> {msg_id}.")
else:
    print("ERROR   > loading -> load messages")
