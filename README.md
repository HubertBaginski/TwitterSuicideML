# TwitterSuicideML

Scripts for reproducing the Machine Learning analysis of the paper: Detecting Potentially Harmful and Protective Suicide-related Content on Twitter: Machine Learning Classification of Tweets

1. clone this repository: 
git clone https://github.com/HubertBaginski/TwitterSuicideML.git

2. Get the dataset with tweet text, and put it in the folder "data" within the repository folder.

The datasets in this repository do not include the text of tweets, in order to protect sensitive user data.  Option a: Rehydrate the IDs via the Twitter API to get all tweets that have not been deleted by their authors in the mean time. This is clearly the preferred option, and aligns with the Twitter Developer Agreement. 

Option b: We will only share data incuding tweet texts under specific conditions: We share the dataset with non-profit organizations, and for projects that clearly benefit the data subjects or have a clear scientific purpose that advances the common interest. Under all circumstances, we will protect users' right to delete their tweets, given the sensitive topic. This means we can only share tweets that were not deleted. If you cannot rehydrate tweets yourself and think your organization and project fits these conditions, you can contact me at metzler@csh.ac.at to get the datasets including tweet text. Please explain your use case in detail to help us make a decision. 

3. Create a virtual environment "TwittersuicideML":
conda create --name TwitterSuicideML

4. Activate the environments after all packages are installed: 
conda activate TwittersuicideML

5. Install all the packages we used, from within the repository folder:
pip install -r requirements.txt

6. Open Jupyter Notebook or Juptyer Lab


