import React, { useCallback, useEffect, useState } from "react";

export const  Formulario = () =>  {
  const [algoritmos, setAlgoritmos] = useState([]);

  useEffect(() => {
    cargarLista();
  }, []);

  const cargarLista = useCallback(() => {
    fetch(
      'http://localhost:8000/api/algoritmos',
      {
        method: 'GET', // *GET, POST, PUT, DELETE, etc.
      })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setAlgoritmos(data)
      });
  }, [])

  return (
    <div className="row">
      <div className="formulario bloque">
        <div>
          <button onClick={cargarLista}>Recargar Lista</button>
        </div>
        <div>
          <select name="algoritmos" id="algoritmos">
            {algoritmos && algoritmos.map(algoritmo => (<option value={"algoritmo"}>{algoritmo}</option>))}
          </select>
          <button>Escoger</button>
        </div>
      </div>
    </div>
  )
}