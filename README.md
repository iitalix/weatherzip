# WeatherZip

WeatherZip is a web application that allows users to enter a ZIP code and retrieve weather data using the [WeatherAPI](https://www.weatherapi.com/). The app is built using Django Rest Framework (backend) and React (frontend).

---

## Features

- Validate user-entered ZIP codes (5-digit format).

- Fetch current weather data, including maximum and minimum temperatures.

- Responsive user interface.

- Backend custom validation for input data.

- Implements Django’s caching framework with a Redis backend to optimize performance and reduce redundant API calls.

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

Install Redis:

- macOS

```bash
brew install redis
brew services start redis
```

- Ubuntu/Debian

```bash
sudo apt update
sudo apt install redis
sudo systemctl enable redis
sudo systemctl start redis
```

- Windows: Use a Redis installer like [Memurai](https://www.memurai.com/) or download the Redis Windows port.

Create a `.env` file in the backend directory and add your [WeatherAPI](https://www.weatherapi.com/) key:

```plaintext
WEATHER_API_KEY=your_actual_api_key_here
```

Run the Django + Redis backend:

```bash
source venv/bin/activate
python manage.py runserver-with-redis
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
npm run dev
```

### **4. Access the Application**

Open your browser and visit:

```arduino
http://localhost:5173
```

The React frontend communicates with the Django backend running at:

```arduino
http://127.0.0.1:8000/api/zip-weather/
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
MIDDLEWARE = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.common.CommonMiddleware',
  ...,
] + MIDDLEWARE
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Local frontend development
    "https://yourfrontenddomain.com",  # Production frontend
]
CORS_ALLOW_ALL_ORIGINS = True # For dev environment only
```

## Approach & Design Decisions

For this project, I opted for a dedicated frontend and backend architecture, leveraging my experience from App Academy in building full-stack applications. I used `ChatGPT 4o` as a reference and learning tool, along with `GitHub Copilot` for syntax assistance.

I prioritized understanding and implementing core features over overengineering, and leveraged Django's strengths where I could (e.g. built-in validation, serializers) to streamline development.

While I did not get around to unit testing, I used incremental testing to validate both frontend and backend functionalities, addressing errors as they arose.

### Backend Development

The backend is built with `Django` and `Django Rest Framework (DRF)`—technologies I learned on-the-fly during this project. I found Django’s structure to be similar to Flask but more opinionated in its design, which actually made it easier for me to learn and build from scratch by providing a clear framework and built-in tools.

To ensure data integrity, validation is handled using `DRF Serializers`, where user-provided ZIP codes are validated with a custom method `(validate_zipcode)`. For error handling, API responses follow structured error messaging, leveraging Django’s built-in `APIView` and exception handling methods.

Weather data is retrieved from `WeatherAPI` and cached using Django’s built-in caching framework with Redis as the backend. This reduces redundant API calls and improves performance by storing responses for frequently searched ZIP codes. Cached responses expire after a set time (e.g., 1 hour), ensuring data remains fresh without overloading the API.

### Frontend Development

The frontend is built with` React`, utilizing the `useState()` hook for local state management, `Axios` for API requests, and conditional rendering for dynamic UI updates.

User input is collected via the `ZipForm` component, which validates and sends ZIP code data to the backend. The weather data response is then passed to the `ZipResults` component as React Props, ensuring a seamless display of results.

### Challenges

This project was as much a learning experience for me as it was a take-home challenge, and I really enjoyed it!

- New technologies
  - Django & DRF
  - Redis (and caching)
  - Axios

I relied on ChatGPT for help setting up the backend and learning about Django and DRF, while applying what I had previously learned about APIs and REST methodology. There were minor tweaks I made such as using GET instead of POST to retrieve data, storing my API KEY in a .env file, and choosing straight-forward code over using 'RegEx' for validation.

ChatGPT was extremely helpful with validation and error-handling. I wanted to leverage the Serializer and APIView to send errors to the frontend and needed some help getting that sorted out.

I spent a lot of time setting up my environment (installing packages). I initially had planned on building the frontend using Tailwind CSS for simplicity, but gave up when I could not get the installation to work. For me, setting up the environment was the most frustrating and grueling roadblock throughout my time on this project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

[WeatherAPI](https://www.weatherapi.com/) for providing the weather data.

Django Rest Framework for the backend.

React for the frontend.

Feel free to replace with your GitHub username and customize the file as needed!
