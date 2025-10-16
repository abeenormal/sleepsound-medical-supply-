from ._anvil_designer import CartTemplate
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Checkout import Checkout


class Cart(CartTemplate):
  def __init__(self,item_name,item_description,it_image,button_callback,item_price, **properties):
   
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.name_label.content = item_name
    self.description_label.content = item_description
    self.image_content.source = it_image
    self.button_callback = button_callback
    self.price_label.text = item_price
    

    get_open_form('Cart')        
     
  def return_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.button_callback()
    
  
  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked"""  
    for i in self.items:
      self.order.append({'item_name':i['product']['name']})
    try:
      charge = stripe.checkout.charge(amount=self.subtotal*100,
                                      currency="USD",
                                      shipping_address=False,
                                      title="SleepSound",
                                      icon_url="_/theme/sleeplogo.png")
    except:
      return

    anvil.server.call('add_order', charge['charge_id'], self.order)

    get_open_form().cart_items = []
    get_open_form().cart_link_click()
    Notification("Your order has been received!").show()
   
    # Any code you write here will run before the form opens.
 
    self.content_panel.add_component(products_panel)

  