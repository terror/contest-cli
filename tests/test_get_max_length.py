from utils import get_max_length
import requests

def test_get_max_length():
    data = requests.get("https://jsonplaceholder.typicode.com/posts")
    assert(get_max_length(data) == 60)