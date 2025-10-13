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


class Cart(CartTemplate):
  def __init__(self, id_name, **properties):

    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.order_id = []
    self.items = id_name

    if self.items == None:
      self.empty_cart_panel.visible = True
      self.column_panel_1.visible = False
      return

    if self.items:
      

    self.repeating_panel_1.items = self.items

    self.total = sum(item['id_name']['price']  for item in self.items)
    self.total_label.text = f"${self.subtotal:.02f}"

   
  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().shop_link_click()

  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked"""  
    for i in self.items:
      self.order.append({'name':i['product']['name']})
    try:
      charge = stripe.checkout.charge(amount=self.subtotal*100,
                                      currency="USD",
                                      shipping_address=True,
                                      title="Cupcakes & Co.",
                                      icon_url="_/theme/cupcake_logo.png")
    except:
      return

    anvil.server.call('add_order', charge['charge_id'], self.order)

    get_open_form().cart_items = []
    get_open_form().cart_link_click()
    Notification("Your order has been received!").show()

    # Any code you write here will run before the form opens.
