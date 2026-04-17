# 🎧 Model Card: VibeMatch Recommender 1.0

---

## 1. Model Name  

VibeMatch Recommender 1.0  

---

## 2. Intended Use  

This recommender is designed to suggest songs based on a user’s preferences such as genre, mood, energy, and acoustic style.  

It assumes that the user’s taste can be represented using a small set of features.  

This system is intended for classroom exploration and learning purposes, not for real-world users.  

---

## 3. How the Model Works  

The model uses a simple scoring system to rank songs.  

Each song has features such as genre, mood, energy, tempo, valence, danceability, and acousticness. The user profile includes preferences like favorite genre, favorite mood, and target energy.  

The system gives points when a song matches the user’s genre or mood. It also calculates similarity based on how close the song’s energy is to the user’s target. A small bonus is added if the acoustic style matches.  

All songs are scored and ranked from highest to lowest, and the top songs are recommended.  

---

## 4. Data  

The dataset is stored in `songs.csv` and contains a small number of songs. Each song includes features such as genre, mood, energy, tempo, valence, danceability, and acousticness.  

I expanded the dataset to include more genres and moods, but it is still limited and does not represent the full diversity of music tastes.  

Some aspects of music, such as lyrics, artist popularity, and user listening history, are not included in the dataset.  

---

## 5. Strengths  

The system works well for clear and simple user profiles. For example, when a user prefers high-energy pop music, the recommender returns songs that match that vibe closely.  

It also provides clear explanations for why songs are recommended, which makes the system easy to understand.  

In many cases, the recommendations matched my expectations based on the user’s preferences.  

---

## 6. Limitations and Bias  

The recommender has a few limitations based on how the scoring logic is designed. It only considers a small set of features such as genre, mood, energy, and acousticness, and does not take into account important factors like lyrics, artist popularity, or user listening history.

One key issue observed during testing is that the system can over-prioritize energy and genre. Songs like Gym Hero appeared across multiple profiles because they matched strong features like high energy, even when other preferences such as mood were different. This shows that the system may overfit to certain features and not fully respect all user preferences.

The dataset is also small, which means some genres and moods are underrepresented. This can reduce diversity in recommendations and create a filter-bubble effect, where similar types of songs are repeatedly suggested instead of introducing variety.

---

## 7. Evaluation  

I evaluated the recommender by testing it with four different user profiles: High-Energy Pop, Chill Lofi, Deep Intense Rock, and an edge-case profile with high energy but a sad mood.

For each profile, I looked at the top 5 recommended songs and checked whether they matched the expected vibe. The High-Energy Pop profile correctly ranked energetic and upbeat songs, while the Chill Lofi profile shifted toward calmer and more acoustic tracks. The Deep Intense Rock profile favored intense, high-energy songs, which showed that the scoring logic was working as intended.

One surprising result came from the edge-case profile. Even though the mood was set to sad, the recommender still returned energetic songs like Gym Hero. This showed that energy and genre were influencing the ranking more strongly than mood, especially when preferences conflict.

I also ran a small experiment by increasing the importance of energy and reducing the importance of genre. After this change, high-energy songs appeared even more frequently across different profiles. This confirmed that changing weights directly affects the behavior of the recommender and can introduce bias toward certain features.

---

## 8. Future Work  

If I continued developing this recommender, I would improve it by adding more features such as lyrics, artist popularity, and user listening history.  

I would also increase the dataset size to improve diversity and reduce bias.  

Another improvement would be balancing feature weights so that no single feature, like energy, dominates the recommendations.  

---

## 9. Personal Reflection  

This project helped me understand how recommendation systems turn data into predictions. I learned that even simple scoring rules can create meaningful recommendations.  

One interesting discovery was how small changes in weights can completely change the results. Increasing the importance of energy caused the system to favor high-energy songs across many profiles.  

This project also changed how I think about music apps. I now understand that recommendations are not always “smart,” but are often based on simple rules that can introduce bias.  
