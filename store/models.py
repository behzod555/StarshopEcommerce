from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
	name = models.CharField(max_length=200, null=True, verbose_name="Имя")
	email = models.CharField(max_length=200)
	tel = models.CharField(max_length=200, verbose_name="Номер телефона")
	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Клиенты'
		verbose_name_plural = "Клиенты"

SUBPRODUCT = (
    ('xiaomi','ТелефоныXiaomi'),
    ('telSamsung', 'ТелефоныSamsung'),
    ('apple','ТелефоныApple'),
	('samsung', 'ТелевизорыSamsung'),
	('lg', 'ТелевизорыLg'),
	('sony', 'ТелевизорыSony'),
	('pylesosy','БытовыеТехникиПылесосы'),
	('stiralki','БытовыеТехникиСтиральные машины'),
	('xolodilniki','БытовыеТехникиХолодильники'),
	('noutbuki','КомпьютерныеТехникиНоутбуки'),
	('monobolki','КомпьютерныеТехникиМоноболки'),
	('monitory','КомпьютерныеТехникиМониторы'),
	('ventilyatory','КлиматическиеТехникиВентиляторы'),
	('konditsionery','КлиматическиеТехникиКондиционеры'),
	('obogrevateli','КлиматическиеТехникиОбогреватели'),
	)

TOTAL = (
	('бытовые-техники','Бытовые-техники'),
	('компьютерная-техника','Компьютерная-техника'),
	('климатическая-техника','Климатическая-техника'),
	('спортивные-товары','Спортивные-товары'),
	('мужские-туфли','Мужские-туфли'),
	('телефоны','Телефоны'),
	('телевизоры','Телевизоры'),

	)




class Product(models.Model):
	name = models.CharField(max_length=200, verbose_name="Название продукта")
	category = models.CharField(max_length=300, choices=TOTAL, verbose_name="Категория")
	subcategory = models.CharField(max_length=300, choices=SUBPRODUCT)
	price = models.FloatField(verbose_name="Цена")
	description = models.TextField(max_length=5000,blank=True, verbose_name="Описание:")
	image = models.ImageField(null=True, blank=True, verbose_name="Изображение")
	novinki = models.BooleanField(default=False, verbose_name="Новинки")
	popularnye = models.BooleanField(default=False, verbose_name="Популарные")




	def __str__(self):
		return self.name

	

	class Meta:
		verbose_name = 'Продукты'
		verbose_name_plural = "Продукты"
        

	@property
	def imageURL(self):
		try:
			url = self.image.url
		except:
			url = ''
		return url
class Notebook(Product):

    diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процессора')
    ram = models.CharField(max_length=255, verbose_name='Оперативная память')
    video = models.CharField(max_length=255, verbose_name='Видеокарта')
    time_without_charge = models.CharField(max_length=255, verbose_name='Время работы аккумулятора')

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)





class Phone(Product):

	diagonal = models.CharField(max_length=255, verbose_name='Диагональ')
	display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
	resolution = models.CharField(max_length=255, verbose_name='Разрешение экрана')
	accum_volume = models.CharField(max_length=255, verbose_name='Объем батареи')
	ram = models.CharField(max_length=255, verbose_name='Оперативная память')
	sd = models.BooleanField(default=True, verbose_name='Наличие SD карты')
	sd_volume_max = models.CharField(
    	max_length=255, null=True, blank=True, verbose_name='Максимальный объем встраивамой памяти')
	main_cam_mp = models.CharField(max_length=255, verbose_name='Главная камера')
	frontal_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальная камера')

	def __str__(self):
		return self.name

#https://gitlab.com/PyCoding1/django3-ecommerce/-/blob/master/mainapp/templates/product_detail.html


class Order(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Клиент")
	tel = models.CharField(max_length=200, null=True, verbose_name="Номер телефона")
	address = models.CharField(max_length=200, null=False, verbose_name="Адрес")
	city = models.CharField(max_length=200, null=False, verbose_name="Город")
	state = models.CharField(max_length=200, null=False, verbose_name="Область")
	date_ordered = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
	complete = models.BooleanField(default=False, verbose_name="Доставлено")
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)
	class Meta:
		verbose_name = 'Заказы'
		verbose_name_plural = "Заказы"		


	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total 

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total 

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, verbose_name="Название товара")

	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True,verbose_name="ID заказа")
	quantity = models.IntegerField(default=0, null=True, blank=True, verbose_name="Количество")
	date_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

	class Meta:
		verbose_name = 'Заказанные товары'
		verbose_name_plural = "Заказанные товары"

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total


class Catalog(models.Model):
	name = models.CharField(max_length=200)
	category = models.CharField(max_length=300, choices=TOTAL)
	subcategory = models.CharField(max_length=300, choices=SUBPRODUCT)
	image = models.ImageField(null=True, blank=True)