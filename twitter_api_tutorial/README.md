# Getting started with the Twitter API v2 using Python

This folder contains the code behind the [medium article](https://medium.com/data-analytics-at-nesta) on collecting Twitter data using Python and the Twitter API v2.

To be able to run the code, you need a [developer account](https://twitter.com/i/flow/login?input_flow_data=%7B%22requested_variant%22%3A%22eyJyZWRpcmVjdF9hZnRlcl9sb2dpbiI6Imh0dHBzOi8vZGV2ZWxvcGVyLnR3aXR0ZXIuY29tL2VuL3BvcnRhbC9wZXRpdGlvbi9lc3NlbnRpYWwvYmFzaWMtaW5mbyJ9%22%7D) (the process is fairly straightforward and is also described in the [medium article](https://medium.com/data-analytics-at-nesta)).

## Tutorial

1. **First part: [Your first Twitter API request](https://github.com/nestauk/dap_medium_articles/blob/3_twitter_api_tutorial/twitter_api_tutorial/Your%20first%20Twitter%20API%20request.ipynb)**
Learn how to make your first Twitter API request and what the collected data looks like.

2. **Second part: [Tweets from the past 7 days](https://github.com/nestauk/dap_medium_articles/blob/3_twitter_api_tutorial/twitter_api_tutorial/Tweets%20from%20the%20past%207%20days.ipynb)**
Code used to collect Twitter data from the past 7 days using the recent search endpoint.

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