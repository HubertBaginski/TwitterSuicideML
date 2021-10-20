import re
import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import WhitespaceTokenizer

smile = " :smiling_face: "
neutralface = " :neutral_face: "
sadface = " :disappointed_face: "
lolface = " :face_with_tears_of_joy: "


def reduce_lengthening(text):
    pattern = re.compile(r"([a-zA-Z])\1{2,}")
    return pattern.sub(r"\1\1", text)


def process_tweet(x):
    x = re.sub('https?://\S+|www\.\S+', ' http ', x)
    eyes = "8:=;"
    nose = "'`_^-"
    smile = ")Dd]}3"
    sad = "([{|/"
    smiles = []
    sadies = []
    lol = []
    for i in eyes:
        lol.append(i + "p")
        lol.append(i + "P")
        for n in nose:
            lol.append(i + n + "p")
            lol.append(i + "P")
        for j in smile:
            smiles.append(i + j)
            for k in nose:
                smiles.append(i + k + j)
        for j in sad:
            sadies.append(i + j)
            for k in nose:
                sadies.append(i + k + j)
    for i in smiles:
        x = x.replace(i, smile)
    for i in sadies:
        x = x.replace(i, sadface)
    for i in lol:
        x = x.replace(i, lolface)
    temp = x.split(" ")
    upper_count = 0
    for i in temp:
        if i.isupper() is True and len(i) > 1:
            upper_count += 1
        if "#" in i:
            check_if_all_caps = i
            if check_if_all_caps.isupper() is True:
                i = i.lower()
                i = i.replace(i[1], i[1].upper())
                temp = i.replace("#", "#")
                x = x.replace(i, temp)
            else:
                temp_hash = re.sub("([A-Z])", " \\1", i)
                x = x.replace(i, temp_hash)
    if ("800-") in x:
        x += " suicide hotline"

    x = x.replace("@TwURL", " http ")
    x = re.sub(r'(\W)(?=\1)', '', x)
    x = re.sub(r'(\D)(?=\1\1)', '', x)
    x = re.sub(r'(?-imsx:(.+)\b(.+))', r'\1 \2', x)
    x = re.sub("\s+", " ", x)
    return x.lower().strip()


def fix_emotes(s, digits=False):
    replaceMe = string.punctuation.replace("'", "").replace("`", "").replace("@", "")
    for i in replaceMe:
        s = s.replace(i, " " + i + " ")
    s = re.sub("(\s')", " ' ", s)
    s = re.sub("('\s)", " ' ", s)
    s = s.replace("mentalhealth", "mental health").replace("_", "")
    if digits is True:
        s = re.sub('\w*\d\w*', '', s)  # remove digits if flag is set
    s = re.sub("\s+", " ", s)
    return s


def process_token_fin(cleaned_text,
                      punct=False, stopWords=False, lemma=False):
    tknzr = WhitespaceTokenizer()
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()

    try:
        lower_case = cleaned_text.apply(tknzr.tokenize)
    except:
        lower_case = tknzr.tokenize(cleaned_text)

    filtered_result = []

    extended_punct = string.punctuation + '“”' + u"\u201D"
    extended_punct = extended_punct.replace("'", "").replace("`", "").replace("@", "")

    for tweet in lower_case:
        temp = []
        for word in tweet:
            if stopWords is True:
                if word not in stop_words:
                    if punct is True:
                        if word not in extended_punct:
                            temp.append(reduce_lengthening(word))
                    elif punct is False:
                        temp.append(reduce_lengthening(word))
            else:
                if punct is True:
                    if word not in extended_punct:
                        temp.append(reduce_lengthening(word))
                elif punct is False:
                    temp.append(reduce_lengthening(word))
        filtered_result.append(temp)
    if lemma is True:
        fin = []
        for tweet in filtered_result:
            temp = []
            for word in tweet:
                temp.append(lemmatizer.lemmatize(word))
            fin.append(temp)
    else:
        fin = filtered_result

    X_train_str = []
    for i in range(0, len(fin)):
        X_train_str.append(" ".join(fin[i]).replace("@ user", "@user"))
    return X_train_str
