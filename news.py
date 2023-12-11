import requests
import json

news_url="http://api.mediastack.com/v1/news"
news_parameters={
    # "date":"2023-12-24",
    "access_key":"3ab5d00c4603adecd4d94f12074ae8c9",
    "country": "cn"
    
    }

    
    
news_response=requests.get(news_url,news_parameters)
parsed_data=(news_response.json())
print(json.dumps(parsed_data,indent=4))

# Check if 'data' key exists in the response
if 'data' in parsed_data:
    articles = parsed_data['data']

    # Iterate through articles and print titles
    for article in articles:
        title = article.get('title', 'Title not available')
        print(title)
else:
    print("No data key found in the response.")





    
    