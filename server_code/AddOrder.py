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
@in_transaction
def add_to_cart(order_id,id_name, description, image, price, email):
  anvil.users.get_user('email')
  app_tables.products.get.product_details('id_name')
  order_id = app_tables.cart.get_order_id()
  if order_id is None:
  # order_id was None, so add the row with a default value.
    app_tables.cart.add_row(order_id="default_order_id", id_name=id_name, price=price, description=description, email=email)
  else:
  # order_id was not None, so use the value from the 10th index.
  app_tables.cart.add_row(order_id=order_id[10], id_name=id_name, price=price, description=description, email=email)

  if order_id is None:
  # order_id was None, so add the row with a default value.
    app_tables.cart.add_row(order_id="default_order_id", id_name=id_name, price=price, description=description, email=email)
else:
  # order_id was not None, so use the value from the 10th index.
  if order_id is None:
    app_tables.cart.add_row(order_id=order_id[10],id_name=id_name,price=price,description=description,email=email)
   
  else:

    order_id = order_id + 10
    app_tables.cart.add_row()

    return
   

def add_order(charge_id, cart_items):
  app_tables.orders.add_row(charge_id=charge_id, order=cart_items)