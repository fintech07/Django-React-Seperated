import React, { useState, useEffect } from "react";
import logo from "./logo.svg";
import axios from "axios";

import "./App.css";

function App() {
  const [scrapes, setScrapes] = useState([]);

  useEffect( () => {
    async function getData() {
      const result = await axios("http://127.0.0.1:8000/api/");
      setScrapes(result.data)
    }
    getData();
  }, []);

  return (
    <div className="App">
      {scrapes.map((item, index) => (
        <div key={index}>
          <h1> {item.title} </h1> <span> {item.description} </span>
        </div>
      ))}
    </div>
  );
}

export default App;
