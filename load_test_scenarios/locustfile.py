from locust import HttpUser, task

class AgenticUser(HttpUser):
    @task
    def hit_agent(self):
        self.client.post("/agent/execute", json={"input": "stress test"})
