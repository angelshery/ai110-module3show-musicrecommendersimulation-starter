"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs
from tabulate import tabulate

def main() -> None:
    songs = load_songs("data/songs.csv") 

    # Starter example profile
    profiles = {
    "High-Energy Pop": {
        "genre": "pop",
        "mood": "happy",
        "energy": 0.85,
        "likes_acoustic": False,
    },
    "Chill Lofi": {
        "genre": "lofi",
        "mood": "chill",
        "energy": 0.40,
        "likes_acoustic": True,
    },
    "Deep Intense Rock": {
        "genre": "rock",
        "mood": "intense",
        "energy": 0.90,
        "likes_acoustic": False,
    },
    "Edge Case Sad but High Energy": {
        "genre": "pop",
        "mood": "sad",
        "energy": 0.90,
        "likes_acoustic": False,
    },
}

    for profile_name, user_prefs in profiles.items():
        recommendations = recommend_songs(user_prefs, songs, k=5)
        print(f"\n=== {profile_name} ===\n")

        table_data = []
        for song, score, explanation in recommendations:
            table_data.append([
                song["title"],
                f"{score:.2f}",
                explanation
            ])

        print(tabulate(table_data, headers=["Song", "Score", "Reason"], tablefmt="grid"))

if __name__ == "__main__":
    main()
