# Twitter Suicide ML

This repository contains the Python code and data for training the machine learning models for the paper: [Detecting Potentially Harmful and Protective Suicide-Related Content on Twitter: Machine Learning Approach](https://www.jmir.org/2022/8/e34705/). For a detailed documentation, see its method section .

## Important note on sharing the dataset: 
The datasets in this repository do not include the text of tweets in order to protect sensitive user data. The Twitter Developer Agreement does not allow sharing the text of tweets, in particular tweets on sensitive topics (like suicidal thoughts). If you require the text of tweets, rehydrate (**see note of caution below**) the IDs via the Twitter API to get all tweets that have not been deleted or set to private by their authors in the meantime. This protects the rights of tweet authors to remove public access to their data or delete it. Alternatively, you could put together your own, similar dataset using our ML models from Huggingface to classify new tweets, to then manually check the tweet categories relevant to your research question before you use the dataset for model training. Our [annotation scheme](https://jmir.org/api/download?alt_name=jmir_v24i8e34705_app2.pdf&filename=5a5265471499223285b7c2c908f61966.pdf) will help you with the category definitions and rules for manual labeling. 

Given that access to the Twitter API is not free anymore, our team is currently developing a new data-sharing policy and solution. At the moment, we can unfortunately not share this dataset. 

* **Note of caution about Tweet IDs**: we recently discovered an error in some of the Tweet IDs in the dataset of this file. While we are working on reconstructing the correct set of IDs, we do not recommend using our dataset. Alternatively, you could check the rehydrated dataset for any tweets that do not seem to fit the category definitions and exclude them from your analysis. 


## Machine Learning Models

The BERT machine learning models are available on Huggingface:

1) Task 1 classifier - 6 main categories (coping, suicidal ideation & attempts, prevention, awareness, suicide case reports, and irrelevant (all other tweets)): https://huggingface.co/HubertBaginski/bert-twitter-main-categories

2) Task 2 classifier: Is a tweet about actual suicide or off-topic (including, for example, sarcastic uses, metaphors, band names etc.): https://huggingface.co/HubertBaginski/bert-twitter-about-suicide

## Steps to reproduce our machine learning analyses: 

1. clone this repository: 
git clone https://github.com/HubertBaginski/TwitterSuicideML.git

2. Get the dataset with tweet text, and put it in the folder "data" within the repository folder.

The datasets in this repository do not include the text of tweets, in order to protect sensitive user data. Rehydrate the IDs via the Twitter API to get all tweets that have not been deleted or made private by their authors in the mean time.

3. Create a virtual environment "TwittersuicideML":
conda create --name TwitterSuicideML

4. Activate the environments after all packages are installed: 
conda activate TwittersuicideML

5. Install all the packages we used, from within the repository folder:
pip install -r requirements.txt

6. Open Jupyter Notebook or Juptyer Lab

## Dataset documentation

**Training data set** (training_posts20201201_main_categories.csv)

- timestamp: publication date and time of the tweet
- tweet_id: ID needed to redownload the tweet via the Twitter API (rehydration)
- set: the subset of the dataset as described in the Manuscript, section "Creating the Annotation Scheme and Labelled Dataset":
    1. inital_training_set_coded_on_CH denotes the about 550 tweets coded on the Crimson Hexagon platform in step 1 of dataset creation. 
    2. reliability_testing_set1 denotes the 500 tweets added in step 2. 
    3. realibility_testing_set2 deontes the remaining tweets added in step 3, until we reached at least 200 per category
    4.   basefrequency denotes the 1000 randomly selected tweets that were added to the training set in step 4
- ambiguous: keywords for tweets the coders found ambiguous at some point during the coding process. E.g. pastsuicidality denotes tweets that speak about suicidality in the past, and implicitly suggest that coping occured, without being explicit.
- notserious_unclear: tweets that are clearly not serious (jokes, metaphors, exaggerations etc) or where it is unclear if they are serious in contrast to sarcastic etc, are marked with a 1. All other tweets get a 0. 
- focus: the problem/suffering vs. solution/coping perspective of the tweet: 0= neither problem solution,1 = problem, 2=solution (see Table 1 in the Manuscript)
- type: denotes the message type (see Table 1 in the Manuscript)
- category: the 12 detailed categories resulting from crossing focus/perspective and type
- category2: an alternative 2nd category that would also fit that was considered during labelling (could be used for multi-label machine learning models). Most tweets do not have a second fitting category. 
- main_category: the 6 categories that models were trained on in the paper (coping, suicidality (=suicidal ideation & attempts), prevention, awareness, werther (=suicide cases) and all other categories combined irrelevant
- about_suicide: tweet is about actual suicide = 1, not about actual suicide = 0. All tweets except the off-topic category are about actual suicide. 



**Number of tweets per category in the dataset**

| Detailed category | n | Main category | About suicide | 
| --- |---|---|---|
| Suicidal ideation & attempts | 284 | Suicidal ideation & attempts| 1 |
| Coping  | 205 | Coping | 1 |
| Awareness  | 314 | Awareness |1 |
| Prevention  | 457 | Prevention |1 |
| Suicide case | 514 | Suicide case |1 |
| News suicidal ideation  | 68 | Irrelevant |1 |
| News coping  | 27 | Irrelevant |1 |
| Bereaved negative | 34 | Irrelevant |1 |
| Bereaved coping | 34 | Irrelevant |1 |
| Live saved | 13 | Irrelevant |1 |
| Suicide other | 440 | Irrelevant |1 |
| Off-topic | 812 | Irrelevant |0|
