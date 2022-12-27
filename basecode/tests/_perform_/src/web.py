from locust import FastHttpUser, task

class Web (FastHttpUser):

    @task
    def index (self) -> None:
        """
        :rtype: None
        """
        self.client.get ("/")
