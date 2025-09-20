from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import json
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Simple knowledge base for the shop
SHOP_KB = {
    "products": {
        "laptop": {"price": "$999", "stock": "In stock", "warranty": "2 years"},
        "phone": {"price": "$699", "stock": "In stock", "warranty": "1 year"},
        "tablet": {"price": "$399", "stock": "Out of stock", "warranty": "1 year"},
        "headphones": {"price": "$199", "stock": "In stock", "warranty": "6 months"}
    },
    "policies": {
        "return": "30-day return policy on all items",
        "shipping": "Free shipping on orders over $50",
        "warranty": "All products come with manufacturer warranty"
    },
    "contact": {
        "phone": "1-800-SHOP-123",
        "email": "support@myshop.com",
        "hours": "Mon-Fri 9AM-6PM"
    }
}

def get_bot_response(user_message):
    message = user_message.lower().strip()
    
    # Greeting patterns
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon"]
    if any(greeting in message for greeting in greetings):
        return "Hello! I'm your shop assistant. How can I help you today? You can ask about products, prices, shipping, returns, or contact information."
    
    # Product inquiries
    for product in SHOP_KB["products"]:
        if product in message:
            info = SHOP_KB["products"][product]
            return f"Our {product} is priced at {info['price']} and is currently {info['stock']}. It comes with {info['warranty']} warranty. Would you like to know anything else about it?"
    
    # Price inquiries
    if "price" in message or "cost" in message or "how much" in message:
        return "I can help you with pricing! We have:\n- Laptop: $999\n- Phone: $699\n- Tablet: $399\n- Headphones: $199\nWhich product are you interested in?"
    
    # Stock/availability
    if "stock" in message or "available" in message or "in stock" in message:
        available = [k for k, v in SHOP_KB["products"].items() if v["stock"] == "In stock"]
        return f"Currently in stock: {', '.join(available)}. Tablet is currently out of stock."
    
    # Shipping inquiries
    if "shipping" in message or "delivery" in message:
        return f"{SHOP_KB['policies']['shipping']}. Standard delivery takes 3-5 business days."
    
    # Return policy
    if "return" in message or "refund" in message:
        return f"{SHOP_KB['policies']['return']}. Items must be in original condition with receipt."
    
    # Contact information
    if "contact" in message or "phone" in message or "email" in message:
        contact = SHOP_KB["contact"]
        return f"You can reach us at:\nPhone: {contact['phone']}\nEmail: {contact['email']}\nHours: {contact['hours']}"
    
    # Warranty inquiries
    if "warranty" in message or "guarantee" in message:
        return "All our products come with warranty:\n- Laptops & Phones: Extended warranty\n- Tablets & Headphones: Standard warranty\nWarranty covers manufacturing defects."
    
    # Default response
    return "I'm here to help! You can ask me about:\n- Product information and prices\n- Stock availability\n- Shipping and delivery\n- Return policy\n- Contact information\n- Warranties\nWhat would you like to know?"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400
        
        bot_response = get_bot_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': 'Something went wrong'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)