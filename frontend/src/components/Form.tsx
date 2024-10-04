import React, { useState } from "react";
import axios from "axios";

const Form: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [result, setResult] = useState(null);
  const [alert, setAlert] = useState(false);

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

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await axios.post(`${apiUrl}/upload`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
          Accept: "application/json",
        },
      });
      setResult(response.data);
    } catch (error) {
      setAlert(true);
      console.log(error);
    }
  };

  const formatResult = (result: JSON) => {
    const output = Object.entries(result)
      .map(
        ([bird, count]) => `${bird[0].toUpperCase() + bird.slice(1)}: ${count}`
      )
      .join("\n");

    if (output) {
      return <div>{output}</div>;
    } else {
      return "No birds found!";
    }
  };

  return (
    <div className="App App-header">
      <h1>How Many Birds Are There?</h1>
      <h4>Check how many birds appear in your pdf file!</h4>
      <form onSubmit={handleFileUpload}>
        <input
          type="file"
          onChange={handleFileChange}
          accept="application/pdf"
        />
        <br />
        <button type="submit">Upload and Analyze</button>
      </form>

      {alert && (
        <div>
          <p> Error uploading pdf. Try again</p>
        </div>
      )}

      {result && (
        <div>
          <h3>Analysis Result:</h3>
          <pre>{formatResult(result)}</pre>
        </div>
      )}
    </div>
  );
};

export default Form;
