// Displays the weather results for a given zip code

const ZipResults = ({ weatherData }) => {
  return (
    <div className="zip-results">
      <h2>
        {weatherData.city}, {weatherData.state}
      </h2>
      <div className="weather-info">
        <div>
          <p id="max-temp">High: {weatherData.maxtemp_f} °F</p>
        </div>
        <div>
          <p id="min-temp">Low: {weatherData.mintemp_f} °F</p>
        </div>
      </div>
    </div>
  );
};

export default ZipResults;
