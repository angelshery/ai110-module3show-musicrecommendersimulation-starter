# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

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

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
