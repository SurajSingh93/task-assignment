from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

# intialize session
session = HTMLSession()

def get_video_metadata(url):
    try:
        video_meta={}
        response = session.get(url)
        response.html.render(timeout=26)
        result = bs(response.html.html, "html.parser")

        video_meta['Url'] = url
        # Video Title
        video_meta["title"] = result.find("h1").text.strip()


        # channel name
        video_meta["channel_name"] = result.find("yt-formatted-string", {"class": "ytd-channel-name"}).find("a").text

        # number of subscribers as str
        video_meta["subscriber"] = result.find("yt-formatted-string", {"id": "owner-sub-count"}).text.strip()

        # Video Views
        video_meta["views"] = int(''.join([c for c in result.find("span", attrs={"class": "view-count"}).text if c.isdigit()]))

        # Video Tags
        video_meta["tags"] = ', '.join(
            [meta.attrs.get("content") for meta in result.find_all("meta", {"property": "og:video:tag"})])

        # Duration of videos
        video_meta["duration"] = result.find("span", {"class": "ytp-time-duration"}).text

        # video description
        video_meta["description"] = result.find("yt-formatted-string", {"class": "content"}).text

        # date published
        video_meta["date_published"] = result.find("div", {"id": "date"}).text[1:]

        # number of likes
        text_yt_formatted_strings = result.find_all("yt-formatted-string",
                                                  {"id": "text", "class": "ytd-toggle-button-renderer"})
        video_meta["likes"] = text_yt_formatted_strings[0].text

        # number of dislikes
        video_meta["dislikes"] = text_yt_formatted_strings[1].text

        # print(video_meta)
        return video_meta
    except:
        print("Try increasing timeout from request process!")
