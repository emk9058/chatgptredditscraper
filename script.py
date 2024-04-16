import praw

client_id = 'g5y3I5vBeSdokQan8iRuNQ'
client_secret = 'yntbv8bWDM6iOzwIY_qBR5my8y7Vhg'
user_agent = 'script:word_count:v1.0 (by u/Cute-Ad-6652)'

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

def count_words(subreddit_name, target_words, limit=500):
    word_count = {word: 0 for word in target_words}
    subreddit = reddit.subreddit(subreddit_name)
    i = 0
    for submission in subreddit.new(limit=limit):
         i+=1
         print(i)
         for word in target_words:
            word_count[word] += submission.title.lower().count(word.lower())
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                word_count[word] += comment.body.lower().count(word.lower())
                
    return word_count

subreddit_name = 'ChatGPTJailbreak'
target_words = ['dan', 'do-anything-now','do anything now','word substitution','word-substitution','substitution','developer mode',
                'developer', 'roleplay', 'role play','role-play', 'aim', 'always intelligent and machiavellian',
                'always intelligent machiavellian', 'ucar', 'universal comprehensive answer resource'
                ,'translatorbot', 'translator bot','translator', 'hypothetical', 'hypotheticals', 'act-like', 'act like']


results = count_words(subreddit_name, target_words)
print(results)
