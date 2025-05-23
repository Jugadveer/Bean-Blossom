from .cart import Cart

#create a context processor so our cart can work on all pages of the website
def cart(request):
    #return the default data from our cart
    return {'cart': Cart(request)}
