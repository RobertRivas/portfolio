import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import './App.css';
import {Home} from "./pages/home";
import {About} from "./pages/about";
import {Contact} from "./pages/contact";
import {EditDistance} from "./pages/editDistance";

function App() {
  return (
    <div className="App">

      <Router>
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/editdistance" element={<EditDistance />} />
        </Routes>



      </Router>









    </div>
  );
}

export default App;
