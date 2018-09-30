from basic_app.forms import OrderForm

def get_order_form(request):
        order_form = OrderForm(user=request.user.id)
        return {'order_form':order_form}
