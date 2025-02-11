import { Route,Routes } from "react-router-dom";

import Home from './pages/Home';
import Reports from './pages/Reports'
import FileInput from './pages/FileInput'


function App() {
    return (
        <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/reports" element={<Reports />}></Route>
            <Route path="/file" element={<FileInput />}></Route>
        </Routes>
    )
}

export default App;
