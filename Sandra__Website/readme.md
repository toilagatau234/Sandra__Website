# 🛍️ Sandra Website – Nền tảng thương mại điện tử

Sandra là một dự án Django xây dựng nền tảng thương mại điện tử với 3 vai trò chính: Người mua, Người bán và Quản trị viên. Dự án hỗ trợ quản lý sản phẩm, đơn hàng, giỏ hàng, thanh toán, gợi ý sản phẩm và chatbot AI.

---

## 🚀 Tính năng chính

- Quản lý người dùng & phân quyền
- Tạo và quản lý sản phẩm, danh mục
- Giỏ hàng & thanh toán (tích hợp MySQL)
- Gợi ý sản phẩm theo hành vi người dùng
- Chatbot AI hỗ trợ người mua
- Dashboard dành cho người bán & admin

---

## 🧰 Công nghệ sử dụng

- **Backend**: Django, Django REST Framework
- **Database**: MySQL (local hoặc Docker)
- **AI**: Tích hợp OpenAI / HuggingFace (tùy chọn)
- **DevOps**: Docker, Docker Compose
- **Frontend**: Django Template / React (tùy chọn)

---

## ⚙️ Cài đặt dự án

### 1. Clone dự án

```bash
git clone https://github.com/toilagatau234/Sandra__Website.git
cd Sandra__Website

### 2. Tạo file .env
Tạo file .env dựa trên mẫu .env.example

### 3. Cài đặt thư viện
    pip install -r requirements.txt

### 4. Tạo database MySQL
Tạo thủ công database sandra__website trong MySQL Workbench hoặc bằng lệnh:
    CREATE DATABASE sandra_website CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

### 5. Chạy migrate & khởi động server
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver


📁 Cấu trúc thư mục
Sandra_Website/
├── apps/
│   ├── users/
│   ├── products/
│   ├── orders/
│   └── ...
├── Sandra_Website/
│   ├── settings.py
│   ├── urls.py
├── templates/
├── static/
├── media/
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md





### bạn có thể chạy docker cho tất cả.
    bạn chạy 2 lệnh: 
        - cp .env.example .env
        - docker-compose up --build