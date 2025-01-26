const ZipResults = ({ weatherData }) => {
  return (
    <>
      <h2>
        {weatherData.city}, {weatherData.state}
      </h2>
      <p>High (°F): {weatherData.maxtemp_f}</p>
      <p>Low (°F): {weatherData.mintemp_f}</p>
    </>
  );
};

export default ZipResults;
