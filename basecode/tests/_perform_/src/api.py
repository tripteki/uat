from locust import FastHttpUser, task

class Api (FastHttpUser):

    @task
    def index (self) -> None:
        """
        :rtype: None
        """
        self.client.get ("/api")
