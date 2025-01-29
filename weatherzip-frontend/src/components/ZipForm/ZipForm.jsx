import { useState } from 'react';
import axios from 'axios';
import ZipResults from '../ZipResults/ZipResults';

const ZipForm = () => {
  const [zip, setZip] = useState('');
  const [weatherData, setWeatherData] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!zip.trim()) {
      setError('Please enter a ZIP code.');
      return;
    }

    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/api/zip-weather/${zip}/`
      );
      setWeatherData(res.data);
      setError(null);
    } catch (err) {
      if (err.response) {
        // Handle errors from the backend
        const backendErrors = err.response.data;

        const errorMessage =
          backendErrors.zipcode?.[0] || // Serializer validation errors
          backendErrors.error || // General errors (e.g., WeatherAPI)
          backendErrors.details?.error?.message || // Specific WeatherAPI errors
          'An error occurred. Please try again.'; // Fallback

        setError(errorMessage);
      } else if (err.request) {
        // No response received from the server
        setError('Unable to reach the server. Please try again later.');
      } else {
        // Other unexpected errors
        setError(
          'An unexpected error occurred. Please try again or contact support.'
        );
      }

      setWeatherData(null); // Clear weather data on error
    }
  };

  return (
    <div id="form-results-container">
      <form onSubmit={handleSubmit} id="zip-form">
        <label className="labels">Enter Your Zip Code</label>
        <div className="input-container">
          <input
            id="input-zip"
            type="text"
            placeholder="eg. 12345"
            value={zip}
            onChange={(e) => {
              setZip(e.target.value);
              setError(null);
              setWeatherData(null);
            }}
          ></input>
          <button id="submit-btn" type="submit">
            Submit
          </button>
        </div>
      </form>
      <div id="results-container">
        {error && <p className="error">{error}</p>}
        {weatherData && <ZipResults weatherData={weatherData} />}
      </div>
    </div>
  );
};

export default ZipForm;
