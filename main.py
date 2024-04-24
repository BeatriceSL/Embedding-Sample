import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
import cohere
co = cohere.Client(os.environ['COHERE_API_KEY'])
import pandas as pd

three_words = pd.DataFrame({'text':
  [
      'joy',
      'happiness',
      'potato'
  ]})

three_words

print(three_words)


