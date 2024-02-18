

from API import get_prediction

# path to trained model
model_path = r"C:/Users/jeyes/Desktop/baselines/Phishing-Attack-Domain-Detection/models/Malicious_URL_Prediction.h5"

# input url
url = "http://pay.91-92-244-213.cprapid.com/bbnl/"

# returns probability of url being malicious
prediction = get_prediction(url,model_path)
print(prediction)

