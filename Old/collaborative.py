import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
movies_df = pd.read_csv('../movies.csv')
ratings_df = pd.read_csv('../ratings.csv')

movie_ratings = pd.merge(ratings_df,movies_df,on='movieId')
movie_ratings.drop('timestamp',axis=1,inplace=True)
movie_ratings_user = movie_ratings.pivot_table(index='userId',columns='title',values='rating')

#handle NaN-values by centering and filling with zeros
avg_ratings = movie_ratings_user.mean(axis=1)
movie_ratings_user =movie_ratings_user.sub(avg_ratings,axis=0)
movie_ratings_user =movie_ratings_user.fillna(0)

def get_recommendations(userId):
    cosine_sim = cosine_similarity(movie_ratings_user, movie_ratings_user)
    similarities = pd.DataFrame(cosine_sim, index=movie_ratings_user.index, columns=movie_ratings_user.index)
    similar_users = similarities.loc[userId].sort_values(ascending=False).head(10).index
    neighbor_ratings = movie_ratings_user.reindex(similar_users)
    recommendations = neighbor_ratings.mean().sort_values(ascending=False)
    return recommendations
#print(get_recommendations(19).head())
def get_influences(userId):
    user_ratings = movie_ratings_user.loc[userId].to_frame()
    user_ratings.rename(columns={'title': 'title', userId: 'rating'})
    print(user_ratings.columns)
    user_ratings = user_ratings.iloc[user_ratings.rating != 0]
    print(type(user_ratings))
    user_ratings = user_ratings.head(10)
    print(type(user_ratings))
    reference = get_recommendations(userId)
    liste = []
    for i in user_ratings.index:
        help = movie_ratings_user.loc[userId,i]
        movie_ratings_user.loc[userId,i] = 0
        recommendations = get_recommendations(userId)
        movie_ratings_user.loc[userId, i] = help
        score = (abs(reference-recommendations)).sum()
        liste.append(score)
    user_ratings['influence'] = liste
    print(user_ratings)
   # user_ratings['influence'] = user_ratings['influence'] / (user_ratings['influence'].max())
   # df = pd.DataFrame(list(zip(user_ratings.index,liste)),columns=['title','ratings'])
    #print(user_ratings)
    #print(df)
    return user_ratings
print(get_influences(19))