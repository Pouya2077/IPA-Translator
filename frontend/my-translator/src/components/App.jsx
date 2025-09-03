import React from "react"
import { BrowserRouter, Routes, Route } from "react-router-dom"
import Translator from "./Translator"
import About from "./About"
import Resources from "./Resources"

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Translator />} />
                <Route path="/about" element={<About />} />
                <Route path="resources" element={<Resources />} />
            </Routes>
        </BrowserRouter>
    )
}

export default App