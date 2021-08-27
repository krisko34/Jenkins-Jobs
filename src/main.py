import slack
import argparse
from argparse import RawTextHelpFormatter

SLACK_HOOK = "" #ADD SLACK HOOK ID
SLACK_CHANNEL = "" #ADD SLACK CHANNEL ID

def main(): 
    parser = argparse.ArgumentParser(
       description="Jenkins current job name.",
       formatter_class=RawTextHelpFormatter)
    
    parser.add_argument("-n", "--hostname", help="Jenkins job name is")
    parser.add_argument("-num", "--jobNumber", help="Number of jenkins job")
    parser.add_argument("-nea", "--nodeExecutedAt", help="Number node on which the job is executed at.")
    parser.add_argument("-url", "--url", help="Url of the job.")
    args = parser.parse_args()
    color = "#fc1500"
    print("Required: Name, number, node, url" .format(args.hostname, args.jobNumber, args.nodeExecutedAt, args.url, color)) 
    client = slack.WebClient(token=SLACK_HOOK)
    print(args.hostname, args.jobNumber, args.nodeExecutedAt, args.url)
    
    block = [ 
         {"type": "section", 
            "text": {
                "type": "mrkdwn", 
                "text": "*Jenkins job cron failed :anger:* "
            }},
            {"type": "section", 
            "text": {
                "type": "mrkdwn", 
                "text": "*Job name:* " + args.hostname,
            }},
            {"type": "section", 
            "text": {
                "type": "mrkdwn", 
                "text": "*Job number:* " + args.jobNumber
            }},        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "*Executed at node number:* " + args.nodeExecutedAt,
            }, 
        }, {"type": "divider"},
            {"type": "section", 
            "text": {
                "type": "mrkdwn", 
                "text": "*Job URL:* " + args.url
            }}, {"type": "divider"},     
    ]

    client.chat_postMessage(channel=SLACK_CHANNEL, blocks=block)

if __name__ == "__main__":
    main()
