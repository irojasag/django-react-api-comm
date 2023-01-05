import React, { useCallback, useEffect, useState } from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const options = {
  responsive: true,
  plugins: {
    legend: {
      position: 'top',
    },
    title: {
      display: true,
      text: 'Chart.js Line Chart',
    },
  },
};

export const  Graficos = () =>  {
  
  const [opciones, setOpciones] = useState([]);
  const [csvData, setCsvData] = useState([]);
  const [datos, setDatos] = useState();
  const [algo1, setAlgo1] = useState(true);
  const [dataSetAUsar, setDataSetAUsar] = useState();

  useEffect(() => {
    cargarDatos();
  }, []);

  const cargarDatos = useCallback(() => {
    // Promises
    fetch(
      'http://localhost:8000/api/algoritmos/ejecutar_algoritmo/1',
      {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        body: {}
      })
      .then((response) => response.json())
      .then((response) => {
        console.log(response);
        setDatos(response)
        // Solo 50 datos
        // setCsvData(response.csvData.slice(0,50));
        // Todos los datos
        setCsvData(response.csvData);
        const elemento = response.csvData[0];
        setOpciones(Object.keys(elemento));
      });
  }, []);

  const generarDataSet = (propiedad) => {
    const dataSet ={
      "labels": Array(csvData.length).fill(''),
      "datasets": [
          {
              "label": propiedad,
              "data": csvData.map(data => data[propiedad]),
              "borderColor": 'rgb(255, 99, 132)',
              "backgroundColor": 'rgba(255, 99, 132, 0.5)',
          }
      ],
    }
    setDataSetAUsar(dataSet);
  }

  return (
    <div className="row">
      <div className="graficos bloque">
        <div>
          <button onClick={cargarDatos}>Recargar datos</button>
          <div>
            {opciones.map((opcion) => (<button onClick={() => generarDataSet(opcion)}>{opcion}</button>))}
          </div>
        </div>
        <div>
          {dataSetAUsar && <Line options={options} data={dataSetAUsar} />}
          {/* <code>{JSON.stringify(csvData)}</code> */}
        </div>
        {datos && <img src={datos.urlImg}/>}
      </div>
    </div>
  )
}







