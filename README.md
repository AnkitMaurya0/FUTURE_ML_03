# 🛍️ Shop Customer Support AI Chatbot

A minimal, lightweight customer support chatbot built with Flask backend and vanilla HTML/CSS/JavaScript frontend. Perfect for small businesses looking to automate customer service without complex AI APIs or expensive solutions.

## ✨ Features

- **Instant Responses** - Handles common customer queries 24/7
- **Product Information** - Provides pricing, stock status, and specifications
- **Policy Support** - Answers questions about shipping, returns, and warranties
- **Contact Integration** - Shares business hours and contact information
- **Mobile Responsive** - Works seamlessly on desktop and mobile devices
- **Real-time Chat** - Modern chat interface with typing indicators
- **Zero Dependencies** - No external AI APIs required

## 🚀 Demo

![Chatbot Demo](demo.gif)

Try asking:
- "What laptops do you have?"
- "What's your return policy?"
- "How much is shipping?"
- "How can I contact you?"

## 🏗️ Architecture

```
┌─────────────────┐    HTTP POST     ┌──────────────────┐
│                 │    /chat         │                  │
│   Frontend      │ ───────────────► │   Flask Backend  │
│   (HTML/CSS/JS) │                  │   (Python)       │
│                 │ ◄─────────────── │                  │
└─────────────────┘    JSON Response └──────────────────┘
```

- **Frontend**: Single HTML file with embedded CSS and JavaScript
- **Backend**: Flask server with rule-based pattern matching
- **Data**: In-memory knowledge base (easily expandable)

## 📁 Project Structure

```
shop-chatbot/
├── app.py                 # Flask backend server
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Frontend interface
└── README.md             # Project documentation
```

## 🛠️ Installation

### Prerequisites
- Python 3.7+ installed
- pip package manager

### Setup Steps

1. **Clone or Download**
   ```bash
   git clone <repository-url>
   cd shop-chatbot
   ```

2. **Create Virtual Environment** (Recommended)
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

5. **Open Browser**
   Navigate to `http://localhost:5000`

## 💬 Bot Capabilities

### Supported Query Types

| Category | Example Queries | Bot Response |
|----------|----------------|--------------|
| **Greetings** | "Hi", "Hello", "Hey" | Welcome message with help options |
| **Products** | "Tell me about laptops", "Phone price" | Product details with price and stock |
| **Pricing** | "How much", "What's the cost" | Complete price list |
| **Inventory** | "What's in stock", "Available items" | Current stock status |
| **Shipping** | "Delivery info", "Shipping cost" | Shipping policies and timeframes |
| **Returns** | "Return policy", "Can I refund" | Return terms and conditions |
| **Contact** | "Phone number", "How to reach you" | Contact information and hours |
| **Warranty** | "Guarantee", "Warranty info" | Warranty terms by product type |

### Sample Conversations

```
User: Hi there!
Bot: Hello! I'm your shop assistant. How can I help you today? You can ask about products, prices, shipping, returns, or contact information.

User: What laptops do you have?
Bot: Our laptop is priced at $999 and is currently In stock. It comes with 2 years warranty. Would you like to know anything else about it?

User: What's your return policy?
Bot: 30-day return policy on all items. Items must be in original condition with receipt.
```

## ⚙️ Customization

### Adding New Products

Edit the `SHOP_KB` dictionary in `app.py`:

```python
SHOP_KB = {
    "products": {
        "laptop": {"price": "$999", "stock": "In stock", "warranty": "2 years"},
        "smartphone": {"price": "$799", "stock": "In stock", "warranty": "1 year"},
        # Add your products here
    }
}
```

### Modifying Responses

Update the `get_bot_response()` function to:
- Add new query patterns
- Customize response messages
- Include additional business logic

### Styling Changes

Modify the CSS in `templates/index.html`:
- Change colors and gradients
- Adjust chat bubble styles
- Update fonts and spacing

## 🔧 Configuration

### Environment Variables

You can configure the app using environment variables:

```bash
export FLASK_ENV=development  # Enable debug mode
export PORT=5000             # Set custom port
```

### Production Deployment

For production deployment:

1. **Set Flask environment**
   ```bash
   export FLASK_ENV=production
   ```

2. **Use production WSGI server**
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. **Deploy to platforms like:**
   - Heroku
   - Digital Ocean
   - AWS EC2
   - Google Cloud Platform

## 📊 Performance

- **Response Time**: < 100ms for typical queries
- **Memory Usage**: ~15MB for basic setup
- **Concurrent Users**: Supports multiple simultaneous conversations
- **Scalability**: Easily scalable with load balancers

## 🧪 Testing

### Manual Testing

Test these scenarios:
- ✅ Greeting responses
- ✅ Product inquiries
- ✅ Policy questions
- ✅ Contact information
- ✅ Unknown queries
- ✅ Empty messages
- ✅ Mobile responsiveness

### Automated Testing

Add test coverage:

```python
# test_chatbot.py
import unittest
from app import get_bot_response

class TestChatbot(unittest.TestCase):
    def test_greeting(self):
        response = get_bot_response("hi")
        self.assertIn("Hello", response)
    
    def test_product_query(self):
        response = get_bot_response("laptop")
        self.assertIn("$999", response)
```

## 🎯 Use Cases

Perfect for:
- **Small E-commerce Stores** - Handle basic customer inquiries
- **Local Businesses** - Provide hours and contact information
- **Service Companies** - Explain policies and procedures
- **Startups** - Cost-effective customer support solution
- **Learning Projects** - Understand chatbot fundamentals

## 🚀 Extensions & Improvements

### Potential Enhancements

1. **Database Integration**
   - PostgreSQL for product data
   - SQLite for conversation history
   - Redis for session management

2. **AI Integration**
   - OpenAI GPT API for complex queries
   - Sentiment analysis
   - Language translation

3. **Advanced Features**
   - User authentication
   - Order tracking integration
   - Live chat handoff to humans
   - Analytics dashboard

4. **UI/UX Improvements**
   - Voice message support
   - File upload capability
   - Chat themes and customization
   - Emoji reactions

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

### Development Guidelines

- Follow PEP 8 for Python code
- Add docstrings for new functions
- Test new features thoroughly
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

### Common Issues

**Q: Chatbot not responding**
- Check if Flask server is running
- Verify browser console for JavaScript errors
- Ensure correct URL (http://localhost:5000)

**Q: CORS errors**
- Flask-CORS is installed and configured
- Check browser's network tab for failed requests

**Q: Mobile layout issues**
- Test with browser dev tools mobile view
- Verify CSS media queries are working

### Getting Help

- 📧 Email: your-email@domain.com
- 💬 LinkedIn: [Your LinkedIn Profile]
- 🐛 Issues: [GitHub Issues Page]

## 🙏 Acknowledgments

- Flask framework for the lightweight backend
- Modern CSS techniques for responsive design
- Pattern matching approach for query processing
- Open source community for inspiration

---

**Built with ❤️ for small businesses and developers learning chatbot fundamentals**

⭐ Star this repository if it helped you build your chatbot!
