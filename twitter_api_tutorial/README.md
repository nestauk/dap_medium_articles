# Getting started with Twitter API v2 using Python

This folder contains the code behind the [medium article](https://medium.com/data-analytics-at-nesta/all-you-need-to-get-started-with-twitter-api-v2-using-python-6cd4be4d90fe) on all you need to get started with Twitter API v2 using Python.

To run the code, you need to [have a developer account](https://developer.twitter.com/en/portal/petition/essential/basic-info) and create an app. The process is fairly straightforward and is also described in the [medium article](https://medium.com/data-analytics-at-nesta/all-you-need-to-get-started-with-twitter-api-v2-using-python-6cd4be4d90fe).

## Tutorial 🤓

1. **[Your first Twitter API request](https://github.com/nestauk/dap_medium_articles/blob/dev/twitter_api_tutorial/Your%20first%20Twitter%20API%20request.ipynb)**

On the first part of this tutorial you will learn how to make your first Twitter API request. This request will output data similar to the mock data below:

```
{'edit_history_tweet_ids': ['100'],
 'author_id': '1',
 'created_at': '2022-11-11T18:25:36.000Z',
 'text': 'I have installed a heat pump in my home!',
 'id': '100'}
```

2. **[Tweets from the past 7 days](https://github.com/nestauk/dap_medium_articles/blob/dev/twitter_api_tutorial/Tweets%20from%20the%20past%207%20days.ipynb)**

On the second part of this tutorial, you will collect Twitter data from the past 7 days using the recent search endpoint. This time, we are collecting additional user information, like in the mock example below:

```
{'id': '987654321',
 'name': 'Number 1 Heat Pump Fan',
 'username': 'heat_pump_fan',
 'description': 'I am a heat pump fan!',
 'location': 'My house in the UK',
 'verified': False}
```

## Set up 🛠️
Open your terminal and follow the instructions:
1. **Clone this repo:** 

`git clone https://github.com/nestauk/dap_medium_articles.git`

2. **Navigate to this tutorial's folder:** 

`cd twitter_api_tutorial`

3. **Create your conda environment:** 

`conda create --name twitter_api_tutorial python=3.9`

4. **Activate your conda environment:** 

`conda activate twitter_api_tutorial`

5. **Install package dependencies:** 

`pip install -r requirements.txt`

6. **Set your credentials as environment variables:** 

`export BEARER_TOKEN="ADD_YOUR_BEARER_TOKEN_HERE"` and replace `ADD_YOUR_BEARER_TOKEN_HERE` with your bearer token credentials.

7. **Add your conda environment to the notebooks:** 

`python -m ipykernel install --user --name=twitter_api_tutorial`

8. **Run the notebooks to collect your own Tweets!** 

Launch `jupyter-notebook` and make sure your kernel is the right environment, `twitter_api_tutorial`.
