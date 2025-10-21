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
  

  def calculate_total(self, cart_items):
    total = sum(self.cart_items['price'] for item in self.items) 
    return total
    

 