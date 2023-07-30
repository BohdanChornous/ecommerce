from django.shortcuts import render
from django.views import View
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
# Create your views here.


class CartSummeryView(View):

    def get(self, request):

        cart = Cart(request)

        return render(request, 'cart/cart-summary.html', context={
            'cart': cart
        })


class CartAddView(View):

    # def get(self, request):
    #
    #     cart = Cart(request)

    def post(self, request):

        cart = Cart(request)
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
        cart_quantity = cart.__len__()

        response = JsonResponse({'qty': cart_quantity,

                                 })
        return response


class CartDeleteView(View):

    def get(self, request):
        pass


class CartUpdateView(View):

    def get(self, request):
        pass
