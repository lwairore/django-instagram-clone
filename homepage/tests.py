from django.test import TestCase
from .models import Image, Follow, Comments, Profile

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        self.image = Image(image_name="Journey at Kisumu", image_caption="Test 2", uploaded_by="James", comments="Nice at Kisuma")

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()

class FollowTestCase(TestCase):
    def setUp(self)
        self.follower = Follow(user_id=1, following_id=5)

    def test_instance(self):
        self.assertTrue(isinstance(self.follower, Follow))

class CommentsTestCase(TestCase):
    def setUp(self):
        self.comment = Comments(comment="Lovely....", image_id=2)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comments))
    
class ProfileTestCase(TestCase):
    def setUp(self):
        self.profile = Profile(user_id=1, first_name="John", last_name="Mikol", email="jkarangu@ghot.com", phone="07289655", bio="Happy love/...")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    


