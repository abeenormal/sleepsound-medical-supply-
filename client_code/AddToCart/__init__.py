from ._anvil_designer import AddToCartTemplate
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


class AddToCart(AddToCartTemplate):
  def __init__(self, id_name, back_button_callback, **properties):
    self.back_button_callback = back_button_callback
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.update_form(id_name)
    # Any code you write here will run before the form opens.

  def update_form(self, id_name):
    products = anvil.server.call("get_product_details", id_name)
    self.products = products
    self.name_label.content = products["name"]
    self.description_label.text = products["description"]
    self.price_label.text = f"${products['price']} USD"
    self.image_content.source = products["image"]

  def add_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.quantity_box.text:
      get_open_form().add_to_cart(self.item, self.quantity_box.text)
      self.quantity_box.text = ""
      self.add_button.visible = False
      self.added_button.visible = True
      self.timer_1.interval = 1
    else:
      self.quantity_box.text = ""
      Notification("Please specify a quantity").show()  

    

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()

  
  def timer_1_tick(self, **event_args):
    """This method is called Every [interval] seconds. Does not trigger if [interval] is 0."""
    self.add_button.visible = True
    self.added_button.visible = False
    self.timer_1.interval = 0
