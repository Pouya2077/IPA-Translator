import { useState } from "react"
import { useNavigate } from "react-router-dom"

function Translator() {
    const [state, setState] = useState(false)
    const navigate = useNavigate()

    const routeTo = (route) => {
        navigate(route)
    }

    return (
        <div>
            <h1>This will be the translator page (home page)</h1>

            <form>
                <label>
                    Enter Sentence
                    <input type="text" />
                    <button type="submit">TRANSLATE</button>
                </label>

            </form>

            <button onClick={() => {routeTo("/about")}}>ABOUT</button>
            <button onClick={() => {routeTo("/resources")}}>RESOURCES</button>

        </div>
    )
}

export default Translator