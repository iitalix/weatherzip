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
      const res = await axios.post('http://127.0.0.1:8000/api/zip-weather/', {
        zipcode: zip,
      });
      setWeatherData(res.data);
      setError(null);
    } catch (err) {
      if (err.response) {
        // Handle validation errors from the serializer
        const backendErrors = err.response.data;
        const errorMessage =
          backendErrors.zipcode?.[0] || // First validation error for the "zipcode" field
          backendErrors.non_field_errors?.[0] || // General validation errors
          'An error occurred. Please try again.';

        setError(errorMessage);
      } else if (err.request) {
        // No response received from the server
        setError('Unable to reach the server. Please try again later.');
      } else {
        // Other unexpected errors
        setError('An unexpected error occurred.');
      }

      setWeatherData(null); // Clear weather data on error
    }
  };

  return (
    <>
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
            }}
          ></input>
          <button id="submit-btn" type="submit">
            Submit
          </button>
        </div>
      </form>
      {weatherData && <ZipResults weatherData={weatherData} />}
      {error && <p className="error">{error}</p>}
    </>
  );
};

export default ZipForm;
