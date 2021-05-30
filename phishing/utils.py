import pandas as pd
import numpy as np
import random
import pickle
import whois
import datetime
import re
from bs4 import BeautifulSoup
import whois
import urllib
import urllib.request
from urllib.parse import urlparse,urlencode
import ipaddress
import requests
# Create your views here.
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import time

def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
    total_Tokens = []
    for i in tkns_BySlash:
        tokens = str(i).split('-')	# make tokens after splitting by dash
        tkns_ByDot = []
        for j in range(0,len(tokens)):
            temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))	#remove redundant tokens
    if 'com' in total_Tokens:
        total_Tokens.remove('com')	#removing .com since it occurs a lot of times and it should not be included in our features
    return total_Tokens


def find_date(url):
  who_is = whois.whois(url)
  if type(who_is.creation_date) is list:
    date_ip_address = who_is.creation_date[0]
  else:
    date_ip_address = who_is.creation_date

  # print(date_ip_address)
  current_time = datetime.datetime.now()
  if date_ip_address is None:

    days = 0
  else:
    actual_time = current_time-date_ip_address
    # print(actual_time)
    days = int(actual_time.days)
    # print(days)
  return days

shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"
def web_traffic(url):
  try:
    #Filling the whitespaces in the URL if any
    url = urllib.parse.quote(url)
    rank = BeautifulSoup(urllib.request.urlopen("http://data.alexa.com/data?cli=10&dat=s&url=" + url).read(), "xml").find(
        "REACH")['RANK']
    rank = int(rank)
  except TypeError:
        return 0
  if rank <100000:
    return 1
  else:
    return 0

def forwarding(response):
  if response == "":
    return 0
  else:
    if len(response.history) <= 2:
      return 0
    else:
      return 1

def rightClick(response):
  if response == "":
    return 0
  else:
    if re.findall(r"event.button ?== ?2", response.text):
      return 1
    else:
      return 0

def mouseOver(response): 
  if response == "" :
    return 0
  else:
    if re.findall("<script>.+onmouseover.+</script>", response.text):
      return 0
    else:
      return 1

def iframe(response):
  if response == "":
      return 0
  else:
      if re.findall(r"[<iframe>|<frameBorder>]", response.text):
          return 1
      else:
          return 0

def redirection(url):
  try:
    pos = url.rfind('//')
    print(pos)
    if pos > 6:
      if pos > 7:
        return 0
      else:
        return 1
    else:
      return 1
  except:
    return 0

def httpDomain(url):
  # domain = urlparse(url).netloc
  # print(domain)
  if 'https' in url:
    return 1
  else:
    return 0

def tinyURL(url):
    match=re.search(shortening_services,url)
    if match:
        return 0
    else:
        return 1

def prefixSuffix(url):
    if '-' in urlparse(url).netloc:
        return 0            # phishing
    else:
        return 1     

def global_variable():
  global x
  global y
  urls_data = pd.read_csv("datasets/urldata.csv")

  y = urls_data["label"]
  url_list = urls_data["url"]
  vectorizer = TfidfVectorizer(tokenizer=makeTokens)
  X = vectorizer.fit_transform(url_list)

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  logit = LogisticRegression()
  x = logit
  return x,X_train,y_train,vectorizer	

def check_url(url):
  start_time = time.time()
  try:
    response = requests.get(url)
  except:
    return "bad"
  url_good_bad = ""
  url_date = find_date(url)

  if url_date < 90:
    url_date_response = 1
  else:
    url_date_response = 0

  web_traffics = web_traffic(url)
  print(web_traffic(url),(time.time() - start_time))
  if web_traffics == 1:
    url_good_bads = "good"
  else:
    url_good_bads = "bad"
  print(url_good_bads,(time.time() - start_time))

  # if xy == "hello":
  #   logit,X_train,y_train,vectorizer = global_variable()
  #   xy = logit
  # logit.fit(X_train, y_train)
  urls_data = pd.read_csv("datasets/urldata.csv")

  # y = urls_data["label"]
  url_list = urls_data["url"]
  vectorizer = TfidfVectorizer(tokenizer=makeTokens)
  X = vectorizer.fit_transform(url_list)

  # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  filename = "datasets/finalized_model.sav"
  loaded_model = pickle.load(open(filename, 'rb'))
  # result = loaded_model.fit(X_train, y_train)
  X_predict=[url]
  X_predict = vectorizer.transform(X_predict)
  New_predict = loaded_model.predict(X_predict)
  print(New_predict,(time.time() - start_time))
  if New_predict[0] == 'good':
    url_good_bad = "good"
    if url_good_bads == "good":
      return url_good_bads
  else:
    url_good_bad = "bad"
  
  redirection_url = redirection(response)
  if redirection_url == 1:
    url_good_bad = "good"
  else:
    url_good_bad = "bad"

  forward_url = forwarding(response)
  if forward_url == 1:
    url_good_bad = "good"
  else:
    url_good_bad = "bad"
  print("Forward URL "+str(forwarding(response)),(time.time() - start_time))
  
  right_click_url = rightClick(response)
  print("Right Click "+str(rightClick(response)),(time.time() - start_time))

  mouse_over_url = mouseOver(response)
  print("Mouse Over "+str(mouseOver(response)),(time.time() - start_time))

  iframe_url = iframe(response)
  print("IFrame "+str(iframe(response)),(time.time() - start_time))
  
  print("HTTP Domain "+str(httpDomain(url)),(time.time() - start_time))
  print("Tiny URL "+str(tinyURL(url)),(time.time() - start_time))
  print("Prefix Suffix "+str(prefixSuffix(url)),(time.time() - start_time))

  good_or_bad = forward_url and right_click_url and mouse_over_url and iframe_url and redirection_url
  if good_or_bad == 0:
    print("Bad URL",(time.time() - start_time))
    return "bad"
  else:
    print("Good Url",(time.time() - start_time))
    return "good"
