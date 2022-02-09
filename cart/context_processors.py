#file created by me
from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}