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
def get_my_products():
  user = anvil.users.get_user()
  if user == None:
    return []

  if not user["purchased_products"]:
    return []

  products = []
  for products in user["purchased_products"]:
    product_info = app_tables.products.get(name=products)
    products=products +product_info
    

    return products
    
    
