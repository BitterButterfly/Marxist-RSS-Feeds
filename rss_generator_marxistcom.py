import requests
from bs4 import BeautifulSoup
from feedgen.feed import FeedGenerator
import os

def generate_rss():
    url = "https://www.marxist.com/"  # Replace with the actual website URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all articles (adjust the selector to match the website's structure)
    articles = soup.find_all('article')

    # Create RSS feed
    fg = FeedGenerator()
    fg.title('Custom News Feed')
    fg.link(href=url, rel='alternate')
    fg.description('RSS feed generated from website.')

    for article in articles[:10]:  # Limit to 10 entries
        title = article.find('h2').text if article.find('h2') else "No Title"
        link = article.find('a')['href'] if article.find('a') else url
        
        entry = fg.add_entry()
        entry.title(title)
        entry.link(href=link)

    # Save to file
    feed_path = os.path.join(os.getcwd(), "news_feed_marxistcom.xml")
    fg.rss_file(feed_path)
    print(f"RSS feed generated at {feed_path}")

if __name__ == "__main__":
    generate_rss()
