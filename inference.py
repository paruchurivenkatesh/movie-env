from env import MovieEnv
from models import Action

env = MovieEnv()

tasks = ["easy", "medium", "hard"]

print("[START]")

for task in tasks:
    obs = env.reset(task)
    total_score = 0

    for step in range(3):

        # Smart rule-based agent (better than random)
        profile = obs.user_profile.lower()

        if "action" in profile:
            recommendation = "Avengers"
        elif "romantic" in profile or "drama" in profile:
            recommendation = "Titanic"
        elif "sci-fi" in profile:
            recommendation = "Interstellar"
        else:
            recommendation = "Inception"

        action = Action(
            action_type="recommend",
            content=recommendation
        )

        obs, reward, done, _ = env.step(action)

        total_score += reward.score

        print(f"[STEP] task={task}, step={step}, reward={reward.score}")

        if done:
            break

    print(f"[END] task={task}, total_score={total_score}")