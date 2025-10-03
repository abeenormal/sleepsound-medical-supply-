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
def get_user_products(user):
    # If the user has no purchased_products, return an empty list immediately.
  if not user['purchased_products']:
   return []

    # Initialize a new, separate list to hold the product information.
  user_products = []

    # Loop through each product ID in the user's purchased_products list.
  for product_id in user['purchased_products']:
      # Retrieve the product's full information from the 'products' data table.
    product_info = app_tables.products.get(id_name=product_id)

      # If a product is found, append it to the new list.
    if product_info:
     user_products.append(product_info)

    return user_products


