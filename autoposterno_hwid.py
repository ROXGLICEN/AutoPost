import requests
import time
import json
from urllib.parse import quote_plus
import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8'] # this is a google public dns server,  use whatever dns server you like here
# as a test, dns.resolver.query('www.google.com') should return an answer, not an exception

def main():

    print("""

    ______               _______ _______ __                    
    |   __ \.-----.--.--.|     __|     __|  |_.-----.----.-----.
    |      <|  _  |_   _||    |  |__     |   _|  _  |   _|  -__|
    |___|__||_____|__.__||_______|_______|____|_____|__| |_____|
                                                                
                                                    

                                                        
        """)
    print("Licensed by #power0068\n")
    print("Our Server: https://discord.gg/9WjKmnuYPc\n")
    time.sleep(1)

    # Write check matching for act-code with hwid, if not matching at all,
    # Write activation_code logic here, check from mongodb, if activation-code found in database, then register, bind the act-code to 
    # the users' hwid, so when next time 

    # Check if the user input is 'Y' or 'y' to proceed
    while True:
        print("Starting the process...\n")


        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'authorization': f"{api_key}"
        }

        last_post_time = {channel: 0 for channel in channels_and_slow_modes}

        def post_to_webhook(webhook_url, content, server_name):
            payload = {
                'content': content,
                'embeds': [
                    {
                        'title': " === Division Line ===", 
                        'description': content,
                        'color': 0x00ff00,
                    }
                ]
            }
            requests.post(webhook_url, json=payload)
            time.sleep(1)

        webhook_enabled = config_data.get("webhook_enabled", False)

        while True:
            for channel, data in channels_and_slow_modes.items():
                slow_mode = data['slow_mode']
                server_name = data['server_name']
                time.sleep(post_interval)
                current_time = time.time()
                time_since_last_post = current_time - last_post_time[channel]

                if time_since_last_post >= slow_mode:
                    # Use the corresponding text for the channel
                    text_to_be_posted = texts_for_channels.get(channel, "")
                    
                    payload = {
                        'content': f"{text_to_be_posted}"
                    }
                    r = requests.post(channel, data=payload, headers=headers)

                    # Check if the message was successfully posted to Discord
                    if r.status_code == 200:
                        last_post_time[channel] = current_time
                        print(f"Message posted to {channel}")

                        # Check if webhook is enabled before posting to webhook
                        if webhook_enabled:
                            post_to_webhook(webhook_url, f"Message Is Posted to {server_name}", server_name)

            time.sleep(1)
##============================config======================================###
with open('config.json', 'r') as file:
    # Step 2: Load the JSON data
    config_data = json.load(file)
   
# Define different texts for each channel
texts_for_channels = config_data.get("texts_for_channels", {})
channels_and_slow_modes = config_data.get("channels_and_slow_modes", {})
api_key = config_data.get("api_key", "")
webhook_url = config_data.get("webhook_url", "")
post_interval = config_data.get("post_interval", "")
##============================config======================================###

main()
   
