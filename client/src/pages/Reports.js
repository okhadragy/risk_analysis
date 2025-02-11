import { useLocation } from 'react-router-dom';
import React from 'react';



function Reports() {
    const locaction = useLocation();
    const data = locaction.state;

    document.querySelector('html').setAttribute("id", "Reports");
   
    const sendDataToStreamlit = (data) => {
        fetch("http://127.0.0.1:5000/streamlit", {
          method: "POST",
          body: JSON.stringify(data),
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Content-Type',
          }
        });
    };
      
    // Usage example
    const status_code = sendDataToStreamlit(data)
    console.log(status_code);

    return (
        <div className="Reports">
            <iframe src="http://localhost:8501/" frameborder="0" 
            marginheight="0" 
            marginwidth="0" 
            width="100%" 
            height="100%" 
            title='charts'
            scrolling="auto"></iframe>
        </div>
    );
}

export default Reports;
