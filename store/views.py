from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
import json
import datetime
from .models import * 
from .forms import *
from .utils import cookieCart, cartData, guestOrder

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	novinki = Product.objects.filter(novinki=True)
	popularnye = Product.objects.filter(popularnye=True)
	context = {'novinki':novinki,'popularnye':popularnye, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/store.html', context)



def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items' : items, 'order' : order, 'cartItems' : cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	user = request.user 
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	
	"""if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)
	if request.method == 'POST':
		order.imya = request.POST.get('name')
		order.familiya = request.POST.get('surname')
		order.email = request.POST.get('email')
		order.tel = request.POST.get('number')
		order.adres = request.POST.get('address')
		order.city = request.POST.get('city')
		order.state = request.POST.get('state')
		order.save()
		if order.save():
			return redirect(request,'store')"""


		

	context = {'items':items,'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	if action=='delete':
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)
	
	tel = data['shipping']['number'],
	address=data['shipping']['address'],
	city=data['shipping']['city'],
	state=data['shipping']['state'],

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id
	order.tel= tel
	order.address=address
	order.city=city
	order.state=state

	if total == order.get_cart_total:
		order.complete = False
	order.save()


	
	return JsonResponse('Payment submitted..', safe=False)



def telefon(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="телефоны")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def televizory(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.filter(category="телевизоры")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def Bytovye(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.filter(category="бытовые-техники")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def Sportivnye(request):

	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	product = Product.objects.filter(category="спортивные-товары")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def Mujskie(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="мужские-туфли")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def Klimaticheskaya(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="климатическая-техника")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)
 

def Komputernaya(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="компьютерная-техника")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def TelefonyXiaomi(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="телефоны",subcategory='xiaomi')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def TelefonyApple(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="телефоны",subcategory='apple')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def TelefonySamsung(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="телефоны",subcategory='telSamsung')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def BytovyePylesosy(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="бытовые-техники",subcategory='pylesosy')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def BytovyeStiralki(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.filter(category="бытовые-техники",subcategory='stiralki')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def BytovyeXolodilniki(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="бытовые-техники",subcategory='xolodilniki')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def KomputernayaNoutbuki(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="компьютерная-техника",subcategory='noutbuki')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def KomputernayaMonobolki(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="компьютерная-техника",subcategory='monobolki')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)	

def KomputernayaMonitory(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="компьютерная-техника",subcategory='monitory')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def KlimaticheskayaVentilyatory(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="климатическая-техника",subcategory='ventilyatory')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)
 
def KlimaticheskayaKonditsionery(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="климатическая-техника",subcategory='konditsionery')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def KlimaticheskayaObogrevateli(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="климатическая-техника",subcategory='obogrevateli')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)
 
def televizorySamsung(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="телевизоры",subcategory='samsung')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context) 

def televizoryLg(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="телевизоры",subcategory='lg')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context) 

def televizorySony(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category="телевизоры",subcategory='sony')


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context) 

def about(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/about.html', context)

def ProductDetails(request,id):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    product = Product.objects.get(id = id)
    context = {'cartItems':cartItems, 'order':order, 'items':items, 'product':product}
    return render(request, 'store/product-details.html', context)


def catalog(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	quantityBytovye = Product.objects.filter(category="бытовые-техники").count()
	quantityKlimaticheskie = Product.objects.filter(category="климатическая-техника").count()
	quantityTelefon = Product.objects.filter(category="телефоны").count()
	quantityTelevizor = Product.objects.filter(category="телевизоры").count()
	quantityTufli = Product.objects.filter(category="мужские-туфли").count()
	quantitySport = Product.objects.filter(category="спортивные-товары").count()
	quantityKomputernaya = Product.objects.filter(category="компьютерная-техника").count()
	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items, 'quantityBytovye':quantityBytovye,
	'quantityKlimaticheskie':quantityKlimaticheskie,
	'quantityTelefon':quantityTelefon,
	'quantityTelevizor':quantityTelevizor,
	'quantityTufli':quantityTufli,
	'quantitySport':quantitySport,
	'quantityKomputernaya':quantityKomputernaya,
	}
	return render(request, 'store/catalog.html', context)


"""def TelefonyXiaomi(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='телефоны', subcategory="xiaomi")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def TelefonyApple(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='телефоны', subcategory="apple")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def TelefonySamsung(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='телефоны', subcategory="Samsung")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def BytovyePylesosy(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='bytovye-texniki', subcategory="pylesosy")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def BytovyeStiralki(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.filter(category='bytovye-texniki', subcategory="stiralki")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def BytovyeXolodilniki(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='bytovye-texniki', subcategory="xolodilniki")

	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def KomputernayaNoutbuki(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='kompyuternaya-texnika', subcategory="noutbuki")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def KomputernayaMonobolki(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='kompyuternaya-texnika', subcategory="monobolki")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)	

def KomputernayaMonitory(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='kompyuternaya-texnika', subcategory="monitory")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def KlimaticheskayaVentilyatory(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='klimaticheskaya-texnika', subcategory="ventilyatory")

	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)
 
def KlimaticheskayaKonditsionery(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='klimaticheskaya-texnika', subcategory="konditsionery")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)

def KlimaticheskayaObogrevateli(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='klimaticheskaya-texnika', subcategory="obogrevateli")



	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context)
 
def televizorySamsung(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='телевизоры', subcategory="samsung")



	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context) 

def televizoryLg(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='телевизоры', subcategory="lg")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context) 

def televizorySony(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']


	products = Product.objects.filter(category='телевизоры', subcategory="sony")


	context = {'products':products, 'cartItems':cartItems, 'order':order, 'items':items}
	return render(request, 'store/product.html',context) 

"""

