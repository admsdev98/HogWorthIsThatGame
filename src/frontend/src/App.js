import "./App.css";
import React, { useState, useRef } from "react";

function App() {
  const buttonText = useRef(null);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  async function retrieveGameInfoHLTB(game) {
    setError(null);
    try {
      const res = await fetch("http://localhost:8000/get-game-info", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: game }),
      });
      if (!res.ok) throw new Error("Error en la respuesta");
      const data = await res.json();
      setResult(data);
    } catch (error) {
      setResult(null);
      setError("Error al obtener la información");
    }
  }

  return (
    <div>
      <h1>How Worth Is That Game</h1>
      <input type="text" placeholder="Escribe aquí" ref={buttonText} />
      <button onClick={() => retrieveGameInfoHLTB(buttonText.current.value)}>
        Obtener info!
      </button>

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ textAlign: "left", whiteSpace: "pre-wrap", marginTop: "20px" }}>
          <h2>RAWG</h2>
          <pre>{JSON.stringify(result.rawg ?? "No data", null, 2)}</pre>

          <h2>HowLongToBeat</h2>
          <pre>{JSON.stringify(result.hltb ?? "No data", null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
