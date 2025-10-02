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
  def __init__(self, id_name, back_button_callback, **properties):
    self.back_button_callback = back_button_callback
    
    # Set Form properties and Data Bindings.
    
    self.init_components(**properties)
    self.update_form(id_name)
    # Any code you write here will run before the form opens.

  def update_form(self, id_name):
    products = anvil.server.call('get_product_details', id_name)
    self.products = products
    self.name_label.content = products["name"]
    self.description_label.text = products['description']
    self.price_label.text = f"${products['price']} USD"
    self.image_content.source = products['image']

  def buy_click(self, **event_args):
    """This method is called when the button is clicked"""
    if anvil.users.get_user() ==None:
      anvil.users.login_with_form()

    user = anvil.users.get_user()
    if user ==None:
      alert("Please sign in!")
      return

    if user["purchased_products"]and self.products["id_name"] in user["purchased_products"]:
      alert("You purchased this item!")
      return

    token, info = stripe.checkout.get_token(amount=self.products["price"]*100, currency="USD", title=self.products["name"], description=self.products["description"])
    try:
      anvil.server.call("charge_user", token, user["email"], self.products["id_name"])
      alert("Success")
    except Exception as e:
      alert(str(e))

  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()



