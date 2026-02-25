import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Products from './componets/Products'

function App() {
  const [products, setProducts] = useState([]);
  const [isLoading, setLoading] = useState(true);

  const laodData = async () => {
    setLoading(true);
    try {
      const response = await fetch("/api/products");
      if(!response.ok) throw Error("Errore nel recupero dati");
      const result = await response.json();
      setProducts(result);

    } catch (e){
      console.error(e);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    laodData()
  }, []);

  return (
    <div>
      <label>test</label>
      <Products products={products} isLoading={isLoading}/>
    </div>
  )
}

export default App
