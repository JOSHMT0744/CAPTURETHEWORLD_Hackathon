import requests
import json
import re
import nltk
from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
nltk.download('stopwords')

### All the functions are defined here ###

def getReceiptInfo(imageFile):
    receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt' # Receipt OCR API endpoint
    r = requests.post(receiptOcrEndpoint, data = { \
      'client_id': 'TEST',        # Use 'TEST' for testing purpose \
      'recognizer': 'auto',       # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
      'ref_no': 'ocr_python_123', # optional caller provided ref code \
      }, \
        files = {"file": open(imageFile, "rb")})
    print(r.text)
    return r.text


def getItemList(info):
    regex = '[0-9.+/\£$()]'
    single_char_regex = '(\\b[a-z] \\b|\\b [a-z]\\b)'
    info_json = json.loads(info)
    items_json = info_json['receipts'][0]['items']
    description_list = []
    for item in items_json:
        description = item['description']
        description = re.sub(regex, "", description).lower()
        description = re.sub(single_char_regex, "", description)
        description = description.split(' ')[len(description.split(' ')) - 1]
        print(description)
        # Ensure there are no duplicates
        if description not in description_list:
            description_list.append(description)
    
    return description_list


def removeStopWords(description_list):
      stop_words = set(stopwords.words('english'))
      filtered_sentence = [item for item in description_list if not item in stop_words]
      return filtered_sentence



#regex = "\[(.*, )*.*(, .*)*WORD(, .*)*'(, .*)*\]"



createRegex()