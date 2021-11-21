import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import cosine_similarity

metadata = pd.read_csv('../movies_metadata.csv', usecols=['title', 'overview'])
metadata = metadata.head(30000)

tfidf = TfidfVectorizer(stop_words='english',min_df=2,max_df=0.7)

metadata['overview'] = metadata['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(metadata['overview'])
tfidf_matrix.astype('float32')

cosine_sim = cosine_similarity(tfidf_matrix)
print(cosine_sim)