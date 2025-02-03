from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(Title='Paella', Price='30', Inventory=15)
        self.item2 = Menu.objects.create(Title='Kefir', Price='3', Inventory=8)
        self.item3 = Menu.objects.create(Title='Salad', Price='4', Inventory=12)

    def test_getall(self):
        fries = Menu.objects.get(Title='Paella')
        kanafa = Menu.objects.get(Title='Kefir')
        salad = Menu.objects.get(Title='Salad')

        self.assertEqual(str(fries), 'Fries : 30')
        self.assertEqual(str(kanafa), 'Kanafa : 3')
        self.assertEqual(str(salad), 'Salad : 4')