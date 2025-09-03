import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import Translator from './components/Translator.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Translator />
  </StrictMode>,
)
