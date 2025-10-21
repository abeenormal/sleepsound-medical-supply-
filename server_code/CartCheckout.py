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
  app_tables.orders.add_row() checkout_id=transaction_details['id'],
    amount=transaction_details['amount'],)

  def charge_user(token, email, amount, currency):
    # Create a new customer or retrieve an existing one and charge them
  # For simplicity, this example just creates a new customer and charges immediately
    try:
    # You might want to link this to your Users table
     user = anvil.stripe.new_customer(email, token) 
     charge = customer.charge(total_amount=amount, currency=currency)
    # Charge the customer   
    
     alert(f"Charge successful for {email}: {charge['id']}")
      # Return useful information to the client
    except Exception as e:
    # If the charge fails, raise an exception to be caught on the client side
     alert(f"Charge failed: {e}")
    raise anvil.server.CallableError(f"Charge failed: {e}")