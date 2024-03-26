import requests
import matplotlib.pyplot as plt
from datetime import datetime, timezone

def scrape_subreddit(subreddit_name, start_epoch, end_epoch):
    url = f"https://api.pushshift.io/reddit/search/comment/?subreddit={subreddit_name}&after={start_epoch}&before={end_epoch}&size=500"
    response = requests.get(url)
    data = response.json()['data']
    
    comments_text = ""
    for comment in data:
        comments_text += comment['body'] + " "
    
    return comments_text

def count_words(text, words):
    word_count = {word: 0 for word in words}
    words = text.lower().split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
    return word_count

def main():
    subreddit_name = "ChatGPTJailbreak"
    
    current_time = int(datetime.now(timezone.utc).timestamp())
    one_year_ago = current_time - (365 * 24 * 60 * 60)
    
    scraped_text = ""
    start_epoch = current_time
    end_epoch = one_year_ago
    while start_epoch > end_epoch:
        text = scrape_subreddit(subreddit_name, end_epoch, start_epoch)
        scraped_text += text
        start_epoch = end_epoch
        end_epoch = start_epoch + (365 * 24 * 60 * 60)
    
    words = input("Enter a list of words separated by spaces: ").split()
    word_counts = count_words(scraped_text, words)
    
    print("Word Counts:")
    for word, count in word_counts.items():
        print(f"{word}: {count}")
    
    # Plotting the bar graph
    plt.bar(word_counts.keys(), word_counts.values())
    plt.xlabel('Words')
    plt.ylabel('Counts')
    plt.title(f'Word Counts in "{subreddit_name}" Subreddit (Past Year)')
    plt.xticks(rotation=45)
    plt.show()

if __name__ == "__main__":
    main()
