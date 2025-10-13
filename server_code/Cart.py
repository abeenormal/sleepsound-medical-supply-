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
def create_checkout_session():
  cart_items = anvil.server.session.get('cart', [])
  if not cart_items:
    raise Exception("Your cart is empty.")

  line_items = []
  for item in cart_items:
    line_items.append({
      'price': item['price_id'],
      'quantity': item['quantity'],
    })

  checkout_session = stripe.checkout.Session.create(
    payment_method_types=['card'],
    line_items=line_items,
    mode='payment',
    success_url=anvil.server.get_app_origin() + '#success',
    cancel_url=anvil.server.get_app_origin() + '#cancel',
  )
  return checkout_session['id']
