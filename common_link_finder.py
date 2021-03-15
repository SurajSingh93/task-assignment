from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import Counter
import argparse
import csv

def url_link_finder(url):
    if url.startswith('http'):
        html = urlopen(url)
    else:
        html = urlopen("http://"+url)
    soup = BeautifulSoup(html.read(), 'lxml')
    links = []
    anchor_text = []
    for link in soup.find_all('a', href=True):
        link_string = link.get('href')
        if link_string.startswith('http'):
            links.append(link_string)   # to extract href links
            anchor_text.append(link.text)   # to append anchor text
    text_list = dict(Counter(anchor_text))  # Count number of occurence of anchor text
    links.insert(0,text_list.copy())    # append anchor tag to list of links

    return links

def argument_pass():
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('filename', type=argparse.FileType('r'))
        args = parser.parse_args()  # take url as argument

        for ul in args.filename.readlines():
            # get the data
            data = url_link_finder(ul)
            dict_text = data[0]
            # appending data to csv
            with open('common_link_finder_result.csv', 'a', newline='',encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["href", "anchor_text", "total_occurence"])
                count = 0
                for at in dict_text:
                    writer.writerow([str(data[1:][count]), str(at) ,dict_text.get(at)])
                    count = count + 1
    except:
        print("Please give valid urls !!")

if __name__ == "__main__":
    try:
        argument_pass()
    except:
        print("Please provide a text file containing Urls !")