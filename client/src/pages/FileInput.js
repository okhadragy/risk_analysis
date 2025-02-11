import {useNavigate} from 'react-router-dom'
import React, { useState } from 'react';


function FileInput() {
  const buttonStyle = {background: 'none',
    color: 'inherit',
    border: 'none',
    padding: 0,
    font: 'inherit',
    cursor: 'pointer',
    outline: 'inherit',
    margin: 0
  }

  document.querySelector('html').setAttribute("id", "FileInput");
  const [selectedFile, setSelectedFile] = useState(null);
  const navigate = useNavigate();
  
  const handleFileChange = (event) => {
    if (event.target.files === undefined) {
      setSelectedFile("");
    } else {
      setSelectedFile(event.target.files[0]);
    }
  };
  
  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await fetch('http://127.0.0.1:5000/analyze', {
        method: 'POST',
        body: formData,
        headers:{
          accept: 'application/json',
          "Access-Control-Allow-Origin": "*"
        }
      });
      // Handle the response from the Streamlit app here
      var data = await response.json()
      if (data.length !== 0){
        navigate("/reports",{state:data});
      }
    } catch (error) {
      // TypeError: Failed to fetch
      console.log('There was an error', error);
    }
    
  };
  
  return (
    <div className="FileInput">
      
      <header> </header>

        <main>
            <h1> Risk Control and Analysis </h1>
        </main>

        <section>
            <form onSubmit={handleSubmit} id='myForm'>
              <label for="file"> Present: </label>
              <input id="file" type="file" onChange={handleFileChange} name='file'/>
              <button id="but1" type="reset" onClick={handleFileChange}> X </button>
              <br />
            </form>
        </section>

        <section>
            <div>
              <nav> <a><button type='submit' form='myForm' style={buttonStyle}> Reports </button> </a> </nav>
            </div>
        </section>
    </div>
  );
}

export default FileInput;
