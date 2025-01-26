# WeatherZip

WeatherZip is a web application that allows users to enter a ZIP code and retrieve weather data using the [WeatherAPI](https://www.weatherapi.com/). The app is built using Django Rest Framework (backend) and React (frontend).

---

## Features

- Validate user-entered ZIP codes (5-digit format).

- Fetch current weather data, including maximum and minimum temperatures.

- Responsive user interface.

- Backend custom validation for input data.

---

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- **Python** (>= 3.9)

- **Node.js** (>= 16.x) and npm or yarn

- **Git**

You will also need an API Key which you can obtain for free at [WeatherAPI.com](https://www.weatherapi.com/).

---

## Installation Instructions

### **1. Clone the Repository**

```bash
git clone https://github.com/yourusername/weatherzip.git
cd weatherzip
```

### **2. Backend Setup (Django)\***

Navigate to the backend directory:

```bash
cd backend
```

Create a virtual environment and activate it:

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the backend directory and add your [WeatherAPI](https://www.weatherapi.com/) key:

```plaintext
WEATHER_API_KEY=your_actual_api_key_here
```

Run the Django server:

```bash
python manage.py runserver
```

### **3. Frontend Setup (React)**

Navigate to the frontend directory:

```bash
cd ../frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm start
```

### **4. Access the Application**

Open your browser and visit:

```arduino
http://localhost:3000
```

The React frontend communicates with the Django backend running at:

```arduino
http://127.0.0.1:8000
```

## Project Structure

```plaintext
weatherzip/
├── backend/
│ ├── api/
│ │ ├── **init**.py
│ │ ├── serializers.py
│ │ ├── urls.py
│ │ ├── views.py
│ ├── weatherzip/
│ │ ├── settings.py
│ │ ├── urls.py
│ ├── manage.py
│ ├── .env
│ ├── requirements.txt
├── frontend/
│ ├── src/
│ │ ├── components/
│ │ │ ├── ZipForm.jsx
│ │ │ ├── ZipResults.jsx
│ ├── package.json
│ ├── .env
```

## Environment Variables

### Backend:

Create a `.env` file in the backend directory with:

```plaintext
WEATHER_API_KEY=your_actual_api_key_here
```

### Frontend:

No additional environment variables are needed for the frontend.

## Troubleshooting

### Common Issues:

Missing [WeatherAPI](https://www.weatherapi.com/) Key:

Ensure your `.env` file contains the correct key in the backend directory.

Restart the backend server after adding the key.

Dependency Errors:

Run the following commands to resolve dependency issues:

```bash
pip install --upgrade pip
npm install
```

CORS Issues:

If the frontend cannot connect to the backend, ensure CORS is enabled in `settings.py` in the backend:

```bash
INSTALLED_APPS += ['corsheaders']
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware'] + MIDDLEWARE
CORS_ALLOW_ALL_ORIGINS = True
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

[WeatherAPI](https://www.weatherapi.com/) for providing the weather data.

Django Rest Framework for the backend.

React for the frontend.

Feel free to replace with your GitHub username and customize the file as needed!
