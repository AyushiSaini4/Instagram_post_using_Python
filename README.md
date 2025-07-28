# Instagram_post_using_Python
Here’s a **README.md** file for your Instagram Poster Streamlit app, tailored for GitHub:

---

### 📄 `README.md`

````markdown
# 📸 Instagram Poster via Facebook Graph API

This Streamlit web app allows users to post images to their Instagram Business accounts using the Facebook Graph API.

---

## 🚀 Features

- Upload a publicly accessible image URL
- Add a custom caption
- Post directly to your Instagram Business account
- Displays feedback from the Facebook API
- Simple and clean UI using Streamlit

---

## 🔧 Requirements

- Python 3.x
- Streamlit
- Requests

Install dependencies using:

```bash
pip install streamlit requests
````

---

## ▶️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/instagram-poster.git
cd instagram-poster
```

### 2. Run the App

```bash
streamlit run instagram_poster.py
```

---

## 🛠️ Setup Requirements

Before using the app, make sure:

1. Your Instagram account is a **Business or Creator** account.
2. It is connected to a **Facebook Page**.
3. You have a valid **Facebook Graph API Access Token** with `instagram_basic`, `pages_show_list`, and `instagram_content_publish` permissions.
4. You have your **Instagram Business User ID** (can be fetched using Graph API).
5. Your image URL is **publicly accessible**.

---

## 🔐 Access Token Caution

> **Never hardcode your access token.** Use environment variables or Streamlit secrets in production.

---

## 📂 File Structure

```
.
├── instagram_poster.py     # Streamlit app code
└── README.md               # Project documentation
```


---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Contributing

Pull requests are welcome! Feel free to open an issue or suggest enhancements.

---

## 📬 Contact

Created with ❤️ by [Ayushi Saini](https://github.com/AyushiSaini4)

````


