import React, { useState } from 'react';
import './Burst.css';
import axios from 'axios';


const Burst = () => {
  const [location, setLocation] = useState('');
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:5000/api/detect-cloud-burst', { location });
      setResult(response.data.message);
    } catch (error) {
      console.error('Error detecting cloud burst:', error);
      setResult('An error occurred while detecting cloud burst.');
    } finally {
      setLoading(false);
    }
  };

  return (
    
    <div className="container">
      <h2>Cloud Burst Detection</h2>
      <form onSubmit={handleSubmit} className="form-group">
        <input
          type="text"
          placeholder="Enter location"
          value={location}
          onChange={(e) => setLocation(e.target.value)}
          className="input-field"
        />
        <button type="submit" className="button" disabled={loading}>{loading ? 'Checking...' : 'Check Cloud Burst'}</button>
      </form>
      {result && <p className="result">{result}</p>}
    </div>
    
  );
};

export default Burst;
