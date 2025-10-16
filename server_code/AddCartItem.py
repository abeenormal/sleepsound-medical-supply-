import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_item_to_session_cart_items(id_name, description, image, price, cart_id):
  if 'cart' not in anvil.server.session:
   anvil.server.session['cart']= []

   cart_items = {'id_name': id_name, 'description': description, 'image': image, 'price': price, 'cart_id': cart_id,}
   anvil.server.session['cart'].append(cart_items)

    
@anvil.server.callable  
def add_to_cart_button_click(self, **event_args):
  # ... get product info (product_id, quantity) from form components ...
  anvil.server.call('add_item_to_session_cart', 'id_name','description','image','price', 'cart_id',)

  


 