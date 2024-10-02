import React, { useState } from "react";
import axios from "axios";

const Form: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState(null);
  const [alert, setAlert] = useState(false);
  const [errMessage, setMessage] = useState(null);

  const apiUrl = process.env.REACT_APP_BACKEND_URL;

  // Handle file selection
  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files) {
      setFile(event.target.files[0]);
    }
  };

  const handleFileUpload = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (!file) {
      setAlert(true);
      return;
    }
    setAlert(false);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(`${apiUrl}/upload`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(response.data);
    } catch (error) {
      setAlert(true);
    }
  };

  return (
    <div>
      <h1>Bird Counter</h1>
      <form onSubmit={handleFileUpload}>
        <input
          type="file"
          onChange={handleFileChange}
          accept="application/pdf"
        />
        <button type="submit">Upload and Analyze</button>
      </form>

      {result && (
        <div>
          <h3>Analysis Result:</h3>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Form;
