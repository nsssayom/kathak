from flask import request
from fbmq import Attachment, Template, QuickReply, Page
import time
from .models import *
from .globals import *
from .graph import *


page = Page(ACCESS_TOKEN) #messenger entity
page.greeting("{{user_first_name}}, Welcome to Circuit House!")

# St #the first messagearting button action
page.show_starting_button("START_PAYLOAD")

# St #callback arguarting Button Callback Handler
@page.callback(['START_PAYLOAD'])
def start_callback(payload, event):
    print("GET STARTED TRIGGERED!")
    sender_id = event.sender_id
    profile = get_user_info(sender_id)
    sender_name = profile['first_name']

    page.typing_on(sender_id)
    time.sleep(.3)
    page.typing_off(sender_id)

    # Conversation Starter
    quick_replies = [
        QuickReply(title="📦 Order Product", payload="PICK_ORDER"),
        QuickReply(title="💁 About Us", payload="PICK_ABOUT")
    ]

    page.send(sender_id,
              sender_name + ", here is some options for you.",
              quick_replies=quick_replies)


page.show_persistent_menu([Template.ButtonPostBack('👀 View Categories', 'MENU_CATEGORY'),
                           Template.ButtonPostBack('🛍 View Cart', 'MENU_CART'),
                           Template.ButtonWeb("🌐 Created by Softopian", "www.softopian.com")])


@page.callback(['MENU_CATEGORY'])
def click_persistent_menu_cat(payload, event):
    print("Selected Category")
    page.send(event.sender_id, template_categories())


@page.callback(['MENU_CART'])
def click_persistent_menu_cart(payload, event):
    print("Selected Cart")
 
    response = template_cart_items(event.sender_id)
    cart_template = response[0]
    isNull = response[1]

    page.typing_on(event.sender_id)
    time.sleep(.8)
    page.typing_off(event.sender_id)

    if isNull:
        quick_replies = [
            QuickReply(title="🛒 Buy something", payload="MENU_CATEGORY")
        ]   
        page.send(event.sender_id, "Your cart is empty. 😞 ", quick_replies=quick_replies)
    
    else:
        page.send(event.sender_id, cart_template)
        
        quick_replies = [
        QuickReply(title="⏭️ Continue Shopping", payload="MENU_CATEGORY"),
        QuickReply(title="🧾 Checkout", payload="CHECKOUT")
        ]

        page.send(event.sender_id,
              "You can continue shoppping or check out if your are done for today!",
              quick_replies=quick_replies)


@app.route('/', methods=['GET'])
def receive_message():
    token_sent = request.args.get("hub.verify_token")
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return "Invalid Request"


@app.route('/', methods=['POST'])
def webhook():
    page.handle_webhook(request.get_data(
        as_text=True), message=message_handler)
    return "ok"


@page.handle_message
def message_handler(event):
    sender_id = event.sender_id
    profile = get_user_info(sender_id)
    sender_name = profile['first_name']
    print(sender_name)
    message = event.message.get('text')
    print(message)
    #cat = Category(message, "Barso re " + message, "Barsabo na" + message)

@page.after_send
def after_send(payload, response):
    print(" Sent=>")

"""
@page.handle_delivery
def handle_delivery(response):
    print("=> Msg delivered")


@page.handle_read
def handle_read(response):
    print("=> Msg Read")
"""

@page.callback(['PICK_ORDER'])
def callback_picked_order(payload, event):
    print("PICKED ORDER")
    page.typing_on(event.sender_id)
    time.sleep(2)
    page.typing_off(event.sender_id)
    page.send(event.sender_id, template_categories())

@page.callback(['CHECKOUT'])
def callback_picked_order(payload, event):
    print("Checkout")
    #page.typing_on(event.sender_id)
    #time.sleep(2)
    #page.typing_off(event.sender_id)
    #page.send(event.sender_id, template_categories())

#Show Item Call back
@page.callback(['SHOW_ITEM_|0'])
def click_item(payload, event):
    click_menu = payload.split('|')[1]
    print("SLECTED CAT ID ", click_menu)
    page.typing_on(event.sender_id)
    time.sleep(2.5)
    page.typing_off(event.sender_id)
    page.send(event.sender_id, template_items(click_menu))

#Add Cart Call Back
@page.callback(['ADD_CART_|0'])
def click_item(payload, event):
    item_id = payload.split('|')[1]
    print("SLECTED ITEM ", item_id)
    
    page.typing_on(event.sender_id)
    time.sleep(.7)
    page.typing_off(event.sender_id)
    
@app.route('/', methods=['POST'])
def webhook():
    page.handle_webhook(request.get_data(
        as_text=True), message=message_handler)
    return "ok"


    quick_replies = [
        QuickReply(title='1', payload='CART_QUANTITY|' + item_id + '|1'),
        QuickReply(title='2', payload='CART_QUANTITY|' + item_id + '|2'),
        QuickReply(title='3', payload='CART_QUANTITY|' + item_id + '|3'),
        QuickReply(title='4', payload='CART_QUANTITY|' + item_id + '|4'),
        QuickReply(title='5', payload='CART_QUANTITY|' + item_id + '|5'),
    ]
    page.send(event.sender_id, "Please choose quantity :",
                        quick_replies=quick_replies)

#Quantity Call Back
@page.callback(['CART_QUANTITY|0|0'])
def click_item(payload, event):
    payload_splited = payload.split('|')
    item_id = payload_splited [1]
    quantity = payload_splited [2]
    
    item = Item.query.filter_by(id = item_id).first()
    print("CHOSEN QUANTITY ", quantity, " of ", item.name)
    Cart(event.sender_id, item, quantity)

    page.typing_on(event.sender_id)
    time.sleep(.3)
    page.typing_off(event.sender_id)
    
    quick_replies = [
        QuickReply(title="⏭️ Continue Shopping", payload="MENU_CATEGORY"),
        QuickReply(title="🛍 View Cart", payload="MENU_CART"),
        QuickReply(title="🧾 Checkout", payload="CHECKOUT")
    ]

    page.send(event.sender_id,
              "Product successfully added to Cart!",
              quick_replies=quick_replies)


#Remove Item Call Back
@page.callback(['REMOVE_FROM_CART_|0|0'])
def click_item(payload, event):
    payload_splited = payload.split('|')
    cart_id = payload_splited [1]
    item_id = payload_splited [2]
    
    Cart_item.remove_item(cart_id, item_id)

    quick_replies = [
        QuickReply(title="⏭️ Continue Shopping", payload="MENU_CATEGORY"),
        QuickReply(title="🛍 View Cart", payload="MENU_CART"),
        QuickReply(title="🧾 Checkout", payload="CHECKOUT")
    ]

    page.send(event.sender_id,
              "Product successfully removed from Cart!",
              quick_replies=quick_replies)


#return Template.Generic instance
def template_categories():
    categories = Category.query.all()
    elements = []
    for category in categories:
        payload = "SHOW_ITEM_|" + str(category.id)
        print ("------->", payload)
        element = Template.GenericElement(category.name,
                                    subtitle = category.description,
                                    image_url = category.thumb_urls,
                                    buttons=[
                                        Template.ButtonPostBack("Show Products", payload)
                                    ])
        elements.append(element)
    return Template.Generic(elements)

#return Template.Generic instance for Items
def template_items(category):
    items = Item.query.filter_by(cat_id = category)
    elements = []
    for item in items:
        payload = "ADD_CART_|" + str(item.id)
        print ("------->", payload)
        element = Template.GenericElement(item.name,
                                    subtitle = str(item.price) + "৳\r\n" + item.description,
                                    image_url = item.thumb_urls,
                                    buttons=[
                                        Template.ButtonPostBack("Add to Cart", payload)
                                    ])
        elements.append(element)
    return Template.Generic(elements, True)


#return Template.Generic instance for Cart
def template_cart_items(user_id):
    cart_id = Cart.query.filter_by(user_id = user_id).first().id
    cart_item_query = Cart_item.query.filter_by(cart_id = cart_id).all()

    elements = []

    for item in cart_item_query:
        item_id = item.item_id
        quantity = item.quantity
        
        print (item_id)
        print (quantity)

        item = Item.query.filter_by(id= item_id).first()

        payload = "REMOVE_FROM_CART_|" + str(cart_id) + "|" + str(item.id)
        print ("------->", payload)
        element = Template.GenericElement(item.name,
                                    subtitle = str(item.price) + "৳ (x" + str(quantity) + ")\r\n" + item.description,
                                    image_url = item.thumb_urls,
                                    buttons=[
                                        Template.ButtonPostBack("Remove from cart", payload)
                                    ])
        elements.append(element)
    
    isNull = False
    if not elements: isNull = True

    return [Template.Generic(elements, True), isNull] 
