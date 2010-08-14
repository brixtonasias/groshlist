from django.contrib import admin
from guide.models import Supermarket, Category, Unit, Currency, ShoppingList, ShoppingItem

class SupermarketAdmin(admin.ModelAdmin):
	pass


class CategoryAdmin(admin.ModelAdmin):
	pass


class UnitAdmin(admin.ModelAdmin):
	pass


class CurrencyAdmin(admin.ModelAdmin):
	pass


class ShoppingListAdmin(admin.ModelAdmin):
	pass


class ShoppingItemAdmin(admin.ModelAdmin):
	pass


admin.site.register(Supermarket, SupermarketAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(ShoppingItem, ShoppingItemAdmin)
