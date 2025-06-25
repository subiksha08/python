# 📦 Supply Chain Management System

A full-stack web application designed to simplify and streamline supply chain operations. Built using **Python Flask** and **MongoDB**, this system offers **role-based dashboards** for suppliers and clients, **real-time updates**, and full **CRUD operations** to manage inventory efficiently.

---

## 🧰 Tech Stack

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python, Flask, Flask-Bcrypt, Flask-CORS
- **Database:** MongoDB Atlas (NoSQL, Cloud-based)

---

## 🎯 Features

✅ **User Authentication**  
- Secure login and signup with password hashing  
- Role-based access: Supplier or Client  

✅ **Role-Based Dashboards**  
- **Supplier Dashboard**: Add, update, delete, and view products  
- **Client Dashboard**: View product listings and supply details  

✅ **CRUD Functionality**  
- Create, Read, Update, and Delete product entries directly from the dashboard  

✅ **Real-Time UI Updates**  
- Instant feedback using AJAX and dynamic rendering  

✅ **MongoDB Integration**  
- Cloud-hosted, scalable database using MongoDB Atlas

✅ **Responsive Design**  
- Custom CSS and HTML; no frameworks like Bootstrap used

---

**Authentication Flow**

Users can sign up as a Supplier or Client

Credentials are securely stored with hashed passwords using Flask-Bcrypt

Upon login, users are redirected to their respective dashboards

---

**Security Notes**

Passwords are never stored in plain text (Bcrypt-hashed)

CORS enabled for controlled cross-origin access

Sessions used to manage authenticated state

---

**📜 License**
This project is licensed under the MIT License — feel free to use, fork, and enhance it.

---

**🙌 Acknowledgments**
Thanks to the open-source community and MongoDB Atlas for providing free tier access to scalable NoSQL databases.

