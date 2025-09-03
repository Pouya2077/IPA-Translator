import { useState } from "react"
import { useNavigate } from "react-router-dom"

function Translator() {
    const [state, setState] = useState(false)
    const navigate = useNavigate()

    const changeToAbout = () => {
        navigate("/about")
    }
    
    const changeToResources = () => {
        navigate("/resources")
    }

    return (
        <div>
            <h1>This will be the translator page (home page)</h1>
            <button onClick={changeToAbout}>ABOUT</button>
            <button onClick={changeToResources}>RESOURCES</button>
        </div>
    )
}

export default Translator