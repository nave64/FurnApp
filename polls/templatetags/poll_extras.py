from django import template
from jalali_date import date2jalali

register = template.Library()


def to_persian_numbers(text):
    """Convert English numbers to Persian numbers"""
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    english_digits = '0123456789'
    
    # Create translation table
    translation_table = str.maketrans(english_digits, persian_digits)
    
    # Convert numbers in the text
    return str(text).translate(translation_table)


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


@register.filter(name='show_jalali_date')
def show_jalali_date(value):
    return date2jalali(value)


@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    formatted_value = '{:,}'.format(value) + ' تومان'
    return to_persian_numbers(formatted_value)


@register.filter(name='discount_price')
def discount_polls(value: int):
    formatted_value = '{:,.0f}'.format(float(value)) + ' تومان'  # Format the value with commas
    return to_persian_numbers(formatted_value)




@register.filter(name='persian_numbers')
def persian_numbers(value):
    """Convert any text with English numbers to Persian numbers"""
    return to_persian_numbers(value)


@register.simple_tag
def multiply(quantity, price, *args, **kwargs):
    return three_digits_currency(quantity * price)
