import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Products from './componets/Products'
import InputForm from './componets/InputForm'

function App() {
  const [products, setProducts] = useState([]);
  const [isLoading, setLoading] = useState(true);
  const [trigger, setTriegger] = useState(false);

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

  const handleInput = async (new_product) => {
    try {
      const response = await fetch("/api/products", {
        method : "POST",
        headers : {"content-type" : "application/json"},
        body : JSON.stringify({...new_product, category_id:1}),
      });

      if(!response.ok) throw Error("Errore inserimento");
      const result = await response.json();
      setTriegger(true);
    } catch (e) {
      console.error(e)
    }
  };

  useEffect(() => {
    laodData()
    setTriegger(false);
  }, [trigger]);

  return (
    <div>
      <label>test</label>
      <Products products={products} isLoading={isLoading}/>
      <InputForm onSave={handleInput} />
    </div>
  )
}

export default App
