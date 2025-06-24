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
          {result.rawg ? (
            <React.Fragment>
              <p><strong>Nombre:</strong> {result.rawg.name ?? "N/A"}</p>
              <p><strong>Puntuación total:</strong> {result.rawg.score ?? "N/A"}</p>
              <p><strong>Duración aproximada:</strong> {result.rawg.playtime ? `${result.rawg.playtime} horas` : "N/A"}</p>
            </React.Fragment>
          ) : (
            <p>No hay datos de RAWG</p>
          )}

          <h2>HowLongToBeat</h2>
          {result.hltb ? (
            <React.Fragment>
              <p><strong>Duración main story:</strong> {result.hltb.main_story ?? "N/A"} horas</p>
              <p><strong>Duración main + extra:</strong> {result.hltb.main_extra ?? "N/A"} horas</p>
              <p><strong>Duración completionist:</strong> {result.hltb.completionist ?? "N/A"} horas</p>
            </React.Fragment>
          ) : (
            <p>No hay datos de HowLongToBeat</p>
          )}

          <h2>Score Final</h2>
          <p>{result.score ?? "No disponible"}</p>
        </div>
      )}
    </div>
  );
}

export default App;
