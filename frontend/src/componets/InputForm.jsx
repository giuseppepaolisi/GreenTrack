import { useState } from "react";

const InputForm = ({onSave}) => {
    const [product, setProduct] = useState({name: "", price: 1, quantity:1});

    const handleSubmit = (e) => {
        e.preventDefault();
        onSave(product);
        setProduct({ name: "", price: 1, quantity: 1 });
    }
    return (
        <div>
            <h3>Inserisci prodotto</h3>
            <form onSubmit={handleSubmit}>
                <label>Nome</label>
                <input type="text" value={product.name} onChange={e => setProduct({...product, name: e.target.value})} />
                <label>Prezzo</label>
                <input type="number" min="1" step="1" value={product.price} onChange={e => setProduct({...product, price: e.target.value})} />
                <label>Quantità</label>
                <input type="number" min="1" step="1" value={product.quantity} onChange={e => setProduct({...product, quantity: e.target.value})} />
                <button type="submit">Invia</button>
            </form>
        </div>
    );
}

export default InputForm