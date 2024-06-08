from django import template 
from django.db.models import Sum
from Wool.models import WoolSupplierQuantity
from django.db.models import Sum

register = template.Library()

# function return sum of wool item 
@register.simple_tag(name='color_total')
def color_total(wool_id):
    return WoolSupplierQuantity.objects.filter(wool_id=wool_id).aggregate(sum=Sum('wool_item_count')).get('sum')

# function return sum of weight total 
@register.simple_tag(name='weight_total')
def weight_total(wool_id):
    return WoolSupplierQuantity.objects.filter(wool_id=wool_id).aggregate(sum=Sum('wool_weight')).get('sum')

# function return sum of weight total 
@register.simple_tag(name='avalibale_color')
def color_avaliable(wool_id):
    return WoolSupplierQuantity.objects.filter(wool_id=wool_id).values('wool_color__color_name').annotate(wcount=Sum('wool_item_count'), qcount=Sum('wool_weight'))

