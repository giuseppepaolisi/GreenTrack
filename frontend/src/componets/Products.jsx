
const Products = ({products, isLoading, onDelete}) => {


    return (
        <div>
            {
                isLoading ?
                <label>Caricamento prodotti...</label>
                :
                products !== null && products !== void 0 ?
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nome</th>
                            <th>Prezzo</th>
                            <th>Quantità</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            products.map((product) => (
                                <tr key={product.id}>
                                    <td>{product.id}</td>
                                    <td>{product.name}</td>
                                    <td>{product.price}</td>
                                    <td>{product.quantity}</td>
                                    <td><button onClick={() => onDelete(product.id)}>Elimina</button></td>
                                </tr>
                            )
                        )}
                    </tbody>
                </table>
                :
                <label>Non ci sono prodotti</label>
            }
        </div>
    );
}

export default Products