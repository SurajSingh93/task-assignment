import csv

def write_csv(data):

    csv_columns = ['Url', 'title', 'channel_name', 'subscriber', 'views', 'tags', 'duration', 'description', 'date_published',
                   'likes', 'dislikes']

    data = [data]

    csv_file = "youtube_data_result.csv"
    try:
        with open(csv_file, 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for d1 in data:
                writer.writerow(d1)
    except IOError:
        print("I/O error")