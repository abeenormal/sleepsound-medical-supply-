import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.

@anvil.server.callable
def add_to_cart(id_name,description,image, price, cart_id):
  cart =  anvil.server.session.get('shopping_cart', {})
  cart[id_name]= cart.get(id_name, 0)
  anvil.server.session['cart_items']= cart
  

@anvil.server.callable
def get_cart_items():
  return anvil.server.session.get('')

