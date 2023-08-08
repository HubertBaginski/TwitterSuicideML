# TwitterSuicideML

For detailed documentation, see the method section of this paper: https://www.jmir.org/2022/8/e34705

Scripts for reproducing the Machine Learning analysis of the paper: Detecting Potentially Harmful and Protective Suicide-related Content on Twitter: Machine Learning Classification of Tweets

1. clone this repository: 
git clone https://github.com/HubertBaginski/TwitterSuicideML.git

2. Get the dataset with tweet text, and put it in the folder "data" within the repository folder.

The datasets in this repository do not include the text of tweets in order to protect sensitive user data. Rehydrate the IDs via the Twitter API to get all tweets that have not been deleted or made private by their authors in the meantime.

3. Create a virtual environment "TwittersuicideML":
conda create --name TwitterSuicideML

4. Activate the environments after all packages are installed: 
conda activate TwittersuicideML

5. Install all the packages we used from within the repository folder:
pip install -r requirements.txt

6. Open Jupyter Notebook or Juptyer Lab

## Machine Learning Models

The final BERT machine learning models are available on Huggingface: 
1) Task 1 classifier - 6 main categories (personal coping stories, suicidal ideation & attempts, suicide case reports, awareness tweets, prevention tweets, and all other tweets): https://huggingface.co/HubertBaginski/bert-twitter-main-categories
2) Task 2 classifier: Is a tweet about actual suicide or not (off-topic, sarcastic, metaphors, etc.): https://huggingface.co/HubertBaginski/bert-twitter-about-suicide

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
