from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Page, Block

class PageURLTests(APITestCase):

    def setUp(self):
        self.page = Page.objects.create(title='Test Page', slug='test-page')
        self.block = Block.objects.create(type='Test Block', content={}, settings={}, pageId=self.page)

    def test_page_list_create_url(self):
        url = reverse('page-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_page_detail_url(self):
        url = reverse('page-detail', args=[self.page.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_block_list_create_url(self):
        url = reverse('block-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_block_detail_url(self):
        url = reverse('block-detail', args=[self.block.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_block_put_url(self):
        url = reverse('block-detail', args=[self.block.id])
        response = self.client.put(url, {'type': 'Test Block', 'content': {}, 'settings': {}, 'pageId': self.page.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_block_delete_url(self):
        url = reverse('block-detail', args=[self.block.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_page_put_url(self):
        url = reverse('page-detail', args=[self.page.id])
        response = self.client.put(url, {'title': 'Test Page', 'slug': 'test-page'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_page_delete_url(self):
        url = reverse('page-detail', args=[self.page.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class BlockOrderUpdateTests(APITestCase):

    def setUp(self):
        self.page = Page.objects.create(title='Test Page', slug='test-page')
        self.block1 = Block.objects.create(type='Test Block 1', content={}, settings={}, pageId=self.page, drag_index=1.0)
        self.block2 = Block.objects.create(type='Test Block 2', content={}, settings={}, pageId=self.page, drag_index=2.0)

    def test_block_order_update(self):
        url = reverse('block-order-update')
        data = {
            "blocks": [
                {"id": self.block1.id, "drag_index": 2.0},
                {"id": self.block2.id, "drag_index": 1.0}
            ]
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)