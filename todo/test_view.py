from django.test import TestCase
from .models import Item


class TestView(TestCase):

    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')


    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')


    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test todo item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        response = self.client.post('/add',{'name': 'Test todo'})
        self.assertRedirects(response, '/')


    def test_can_delete_item_page(self):
        item = Item.objects.create(name='Test todo item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        existing_item = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_item),0)

    def test_can_toggle_item_page(self):
        item = Item.objects.create(name='Test todo item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        toggle_item = Item.objects.get(id=item.id)
        self.assertFalse(toggle_item.done)

    def test_can_edit_item_page(self):
        item = Item.objects.create(name='Test todo item')
        response = self.client.post(f'/edit/{item.id}',{'name': 'New name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'New name')

