

from API import get_prediction
# input url
url = "http://pay.91-92-244-213.cprapid.com/bbnl/"

# returns probability of url being malicious
prediction = get_prediction(url)
print(prediction)

