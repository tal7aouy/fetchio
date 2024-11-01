# 📦 Fetch HTTP Library

**Fetch HTTP Library**! is a library that provides a simple and efficient way to make HTTP requests in Python. It supports GET, POST, PUT, and DELETE methods, and handles responses gracefully.

## 🚀 Features

- 🌐 **GET** requests
- 📤 **POST** requests
- ✏️ **PUT** requests
- ❌ **DELETE** requests
- 📦 Singleton pattern to ensure a single instance
- 🛠️ Easy to use and extend
- 📝 Logging for better traceability

## 📚 Installation

To install the required dependencies, run:

```sh
pip install fetchio
```

## 🛠️ Usage

Here's a quick example of how to use the Fetch HTTP Library:

```python
from fetchio.http import Http

http = Http()

# GET request
response = http.get('http://example.com')
print(response)

# POST request
response = http.post('http://example.com', json={'data': 'value'})
print(response)

# PUT request
response = http.put('http://example.com', json={'data': 'value'})
print(response)

# DELETE request
response = http.delete('http://example.com')
print(response)
```

## 🧪 Running Tests

To run the tests, make sure you have `pytest` installed. Then, run the tests with:

```sh
pytest
```

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 📞 Contact

For any questions or inquiries, please contact us at [tal7aouy@gmail.com](mailto:tal7aouy@gmail.com).

---

Made with ❤️ by Mhammed Talhaouy