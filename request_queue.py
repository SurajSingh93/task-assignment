from request_process import get_video_metadata
from request_save import write_csv
import argparse

def argument_pass():
    try:
        parser = argparse.ArgumentParser(description="YouTube Video Data Extractor")
        parser.add_argument("url", help="URL of the YouTube video")
        args = parser.parse_args()
        url = args.url

        # get the data
        data = get_video_metadata(url)
        print(f"Title: {data['title']}")
        print(f"Video tags: {data['tags']}")
        print(f"Views: {data['views']}")
        print(f"Published/Upload Date: {data['date_published']}")
        print(f"Channel/Uploader Title: {data['channel_name']}")
        print(f"Channel/Uploader Subscribers: {data['subscriber']}")
        print(f"\nDescription: {data['description']}\n")
        print(f"\nVideo Duration: {data['duration']}")
        print(f"Likes: {data['likes']}")
        print(f"Dislikes: {data['dislikes']}")

        write_csv(data)
    except:
        print("Please pass youtube link in the parameter !!")

if __name__ == "__main__":
    try:
        argument_pass()
    except:
        print("Inappropirate Url !!")