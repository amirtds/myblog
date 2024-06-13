from locust import HttpUser, between, task
import random

class BlogUser(HttpUser):
    wait_time = between(1, 3)  # Users wait 1-3 seconds between tasks
    post_urls = ["/post/post1", "/post/post2", "/post/post3", "/post/post4", "/post/post5", "/post/post6"]

    @task
    def index_page(self):
        self.client.get("/")

    @task(3)
    def view_post(self):
        post_url = random.choice(self.post_urls)
        self.client.get(post_url)
