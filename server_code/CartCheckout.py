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
def get_session_cart_items():
  return anvil.server.session.get("cart-items", [])

@anvil.server.callable
def clear_cart():
  anvil.sever.session['cart'] = {}

@anvil.server.callable
def process_order(transaction_details):
  app_tables.orders.add_row() (checkout_id=transaction_details['id'], amount=transaction_details['amount'],)

@anvil.server.callable
def charge_user(token, email, cart_items):

  try:
    stripe_customer = anvil.stripe.new_customer(email, token)
    total_amount = sum(item['price'] * 100 for item in cart_items)
    charge = stripe_customer.charge(amount=int(total_amount * 100), currency="USD") 
  except Exception as e:
    alert(str(e))
    if charge['status'] == 'succeeded':
      return {"status": "success", "charge_id": charge['id']}
    else:
      return {"status": "failed", "message": f"Payment status: {charge['status']}"}

