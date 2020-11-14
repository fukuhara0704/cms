from django.contrib import admin
from .models import Member
from .models import Order
from .models import Drink
from .models import MenuCategory
from .models import Goods

admin.site.register(Member)
admin.site.register(Order)
admin.site.register(Drink)
admin.site.register(MenuCategory)
admin.site.register(Goods)
