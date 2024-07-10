from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('catalog/', views.catalog, name="catalog"),
	path('checkout/', views.checkout, name="checkout"),
	path('products/<int:id>/', views.ProductDetails, name='productdetails'),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('catalog/telefony/', views.telefon, name="telefon"),
	path('catalog/televizory/', views.televizory, name="televizory"),
	path('catalog/bytovye-texniki/', views.Bytovye, name="Bytovye"),
	path('catalog/komputernaya-texnika/', views.Komputernaya, name="Komputernaya"),
	path('catalog/klimaticheskaya-texnika/', views.Klimaticheskaya, name="Klimaticheskaya"),
	path('catalog/sportivnye-tovary/', views.Sportivnye, name="Sportivnye"),
	path('catalog/mujskie-tufli/', views.Mujskie, name="Mujskie"),
	path('catalog/telefony/xiaomi/', views.TelefonyXiaomi, name="TelefonyXiaomi"),
	path('catalog/telefony/apple/', views.TelefonyApple, name="TelefonyApple"),
	path('catalog/telefony/samsung/', views.TelefonySamsung, name="TelefonySamsung"),
	path('catalog/bytovye-texniki/pylesosy/', views.BytovyePylesosy, name="BytovyePylesosy"),
	path('catalog/bytovye-texniki/stiralnye-mashiny/', views.BytovyeStiralki, name="BytovyeStiralki"),
	path('catalog/bytovye-texniki/xolodilniki/', views.BytovyeXolodilniki, name="BytovyeXolodilniki"),
	path('catalog/komputernaya-texnika/noutbuki/', views.KomputernayaNoutbuki, name="KomputernayaNoutbuki"),
	path('catalog/komputernaya-texnika/monobolki/', views.KomputernayaMonobolki, name="KomputernayaMonobolki"),
	path('catalog/komputernaya-texnika/monitory/', views.KomputernayaMonitory, name="KomputernayaMonitory"),
	path('catalog/klimaticheskaya-texnika/ventilyatory/', views.KlimaticheskayaVentilyatory, name="KlimaticheskayaVentilyatory"),
	path('catalog/klimaticheskaya-texnika/konditsionery/', views.KlimaticheskayaKonditsionery, name="KlimaticheskayaKonditsionery"),
	path('catalog/klimaticheskaya-texnika/obogrevateli/', views.KlimaticheskayaObogrevateli, name="KlimaticheskayaObogrevateli"),
	path('catalog/televizory/samsung/', views.televizorySamsung, name="televizorySamsung"),
	path('catalog/televizory/lg/', views.televizoryLg, name="televizoryLg"),
	path('catalog/televizory/sony/', views.televizorySony, name="televizorySony"),
	path('company/',views.about, name="about")
]
