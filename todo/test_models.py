from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_done_false(self):
        item = Item.objects.create(name='Test todo')
        self.assertFalse(item.done)

    def test_item_string_method_return_name(self):
        item = Item.objects.create(name='Test todo')
        self.assertEqual(str(item),'Test todo')
