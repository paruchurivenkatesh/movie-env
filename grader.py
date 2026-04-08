def grade_recommendation(recommendation: str, target_movies: list):
    recommendation = recommendation.lower()

    for movie in target_movies:
        if movie.lower() in recommendation:
            return 1.0

    # partial reward
    if any(word in recommendation for word in ["action", "romantic", "sci-fi"]):
        return 0.5

    return 0.0