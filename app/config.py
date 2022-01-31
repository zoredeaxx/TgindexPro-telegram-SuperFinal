import traceback
import json
import sys
import os


try:
    port = int(os.environ.get("PORT", "8080"))
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = int(os.environ.get("API_ID", "7523379"))
    api_hash = os.environ.get("API_HASH", "ce43762f206dc2a2eb115986fbe3b4a2")
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the API_ID and API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

try:
    # index_settings_str = os.environ["INDEX_SETTINGS"].strip()

    # index_settings = json.loads(index_settings_str)

    index_settings = {
      "index_all": False,
      "index_private":True,
      "index_group": True,
      "index_channel": True,
      "exclude_chats": [],
      "include_chats": [int(os.environ.get("INDEXING_CHAT","-1001308033853"))],#my index chat
      "otg": {
          "enable": True,
          "include_private": True,
          "include_group": True,
          "include_channel": True
      }
    }
    otg_settings = index_settings['otg']
    enable_otg = otg_settings['enable']
except:
    traceback.print_exc()
    print("\n\nPlease set the INDEX_SETTINGS environment variable correctly")
    sys.exit(1)

try:
    session_string = os.environ.get("SESSION_STRING", "1BVtsOHIBu052l4e40k0D6RoSOhodMnX8NLGcZZMLt-KKbZwkSD9umJ7WrmuCjqYxQqR0KMYWku8DM6iINchWQTU7TpoPxHDquJ0CJTm8gXYGTIoIQMqpGHGOsS8jGtWgH9IlDFvIRTNTEbFdkBqVxitxKSbEnWS95l1u20UPLEMIBwTM6T0VbJmHw1GHbI_FIaSflHokFLMXw8y5NqNpwOAvGkhT9XoAOT5MCRB6I7fSMdwi0BE5cBNeOnY4FbrYvjsqTJHvj0DMVPsJEpHM2RguCMHK-Zi4W4WXQWko-YsFRQ7xIs0itEhM7yQV6JUS1TYD7Vrzhe3hzllW-nVqTgO-SaVxlt4=")
except (KeyError, ValueError):
    traceback.print_exc()
    print("\n\nPlease set the SESSION_STRING environment variable correctly")
    sys.exit(1)

# try:
#     bot_token = os.environ["BOT_TOKEN"]
# except (KeyError, ValueError):
#     traceback.print_exc()
#     print("\n\nPlease set the BOT_TOKEN environment variable correctly")
#     sys.exit(1)



host = os.environ.get("HOST", "0.0.0.0")
debug = bool(os.environ.get("DEBUG"))
chat_ids = []
alias_ids = []
