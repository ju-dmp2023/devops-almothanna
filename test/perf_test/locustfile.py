from locust import HttpUser, task, between
import random

class CalculatorUser(HttpUser):
    # Requirement: Active users enter a new input every 2 to 4 seconds
    wait_time = between(2, 4)

    # Requirement: Add is used twice as often as other methods (Weight = 2)
    @task(2)
    def add(self):
        payload = {
            "operation": "add",
            "operand1": random.randint(1, 100),
            "operand2": random.randint(1, 100)
        }
        with self.client.post("/calculate", catch_response=True, name='add', json=payload) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status {response.status_code}")

    # Weight = 1 for the rest
    @task(1)
    def subtract(self):
        payload = {
            "operation": "subtract",
            "operand1": random.randint(1, 100),
            "operand2": random.randint(1, 100)
        }
        with self.client.post("/calculate", catch_response=True, name='subtract', json=payload) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status {response.status_code}")

    @task(1)
    def multiply(self):
        payload = {
            "operation": "multiply",
            "operand1": random.randint(1, 100),
            "operand2": random.randint(1, 100)
        }
        with self.client.post("/calculate", catch_response=True, name='multiply', json=payload) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status {response.status_code}")

    @task(1)
    def divide(self):
        # We avoid 0 here to prevent intentional divide-by-zero errors initially
        payload = {
            "operation": "divide",
            "operand1": random.randint(1, 100),
            "operand2": random.randint(1, 100)
        }
        with self.client.post("/calculate", catch_response=True, name='divide', json=payload) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Failed with status {response.status_code}")