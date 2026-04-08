from models import Action, Observation, Reward
from tasks import TASKS
from grader import grade_recommendation

class MovieEnv:

    def __init__(self):
        self.task_name = None
        self.task = None
        self.history = []
        self.done = False

    def reset(self, task_name="easy"):
        self.task_name = task_name
        self.task = TASKS[task_name]
        self.history = []
        self.done = False

        return Observation(
            user_profile=self.task["user_profile"],
            history=[],
            last_feedback=None
        )

    def step(self, action: Action):
        if self.done:
            return None, Reward(score=0), True, {}

        reward = 0.0

        # penalty for repeating same recommendation
        if action.content in self.history:
            reward -= 0.2

        self.history.append(action.content)

        if action.action_type == "ask":
            reward += 0.2
            feedback = "User provided more preferences."

        elif action.action_type == "recommend":
            score = grade_recommendation(
                action.content,
                self.task["target"]
            )

            reward += score

            if score > 0.8:
                reward += 0.3
                self.done = True

            feedback = "Good recommendation!" if score > 0.8 else "Not relevant"

        return (
            Observation(
                user_profile=self.task["user_profile"],
                history=self.history,
                last_feedback=feedback
            ),
            Reward(score=round(reward, 2)),
            self.done,
            {}
        )

    def state(self):
        return {
            "task": self.task_name,
            "history": self.history,
            "done": self.done
        }