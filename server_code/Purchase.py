
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
def charge_user(token,email,product_name):
  stripe_customer = anvil.stripe.new_customer(email, token)
  price = app_tables.products.get(id_name=product_name)['price']
  user = anvil.users.get_user()
  if user["purchased_products"] is None:
    user["purchased_products"] = []

  if product_name in user["purchased_products"]:
    return
  result = stripe_customer.charge(amount=price*100, currency="USD")
  user ["purchased_products"] = user["purchased_products"] + [product_name]