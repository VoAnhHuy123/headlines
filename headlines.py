from flask import Flask
import feedparser


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
            'cnn': 'http://rss.cnn.com/rss/edition.rss',
            'fox': 'http://feeds.foxnews.com/foxnews/latest',
            'iol': 'http://www.iol.co.za/cmlink/1.640',
            'vnexpress': 'https://vnexpress.net/rss/tin-moi-nhat.rss'}


@app.route("/")
@app.route('/<publication>')
def get_news(publication="vnexpress"):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    # print(first_article)
    return """<html>
        <body>
            <h1> BBC Headlines </h1>
            <b>{0}</b> <br/>
            <b>{1}</b> <br/>
        </body>
    </html>""".format(first_article.get("title"), first_article.get("published"))


if __name__ == "__main__":
    app.run(port=5000, debug=True)