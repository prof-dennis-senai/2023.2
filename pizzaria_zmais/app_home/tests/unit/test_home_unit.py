from django.urls import reverse

# Create your tests here.
def test_url_home():
    url = reverse('home')
    assert url == '/'