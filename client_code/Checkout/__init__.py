from ._anvil_designer import CheckoutTemplate
from anvil import *
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe



class Checkout(CheckoutTemplate):
  def __init__(self, cart_items, back_button_callback, **properties):
    self.back_button_callback = back_button_callback
    
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.display_cart_items()
        
    # Any code you write here will run before the form opens.
  def display_cart_items(self):
    self.cart_items = anvil.server.call('get_session_cart-items')
  
    

  def add_order(self, charge_id, cart_items):
    app_tables.orders.add_row(charge_id=charge_id, order=cart_items)
  
  

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()

# In a Form:

  def checkout_button_click(self, **event_args):
   """This method is called when the button is clicked"""
  total_amount = self.calculate_total() # Assuming this method returns the amount in the lowest unit (e.g., cents)
  currency = "USD" # Currency code should be a string, e.g., "USD"

  try:
  # Get the token and user info from the Stripe checkout form
    token, info = stripe.checkout.get_token(amount=total_amount, currency=currency)

  # Call a server-side function to process the charge
    charge_result = anvil.server.call('charge_user', token, info['email'], total_amount, currency)

  # Handle success (e.g., show a confirmation message)
    alert(f"Payment succeeded! Transaction ID: {charge_result['id']}")
  except stripe.checkout.Canceled:
  # Handle the case where the user cancels the payment
    alert("Payment cancelled.")
  except anvil.server.CallableError as e:
  # Handle errors from the server-side function
    alert(f"Payment failed: {e.args[0]}")
  except Exception as e:
  # Handle any other unexpected errors
    alert(f"An unexpected error occurred: {e}")




