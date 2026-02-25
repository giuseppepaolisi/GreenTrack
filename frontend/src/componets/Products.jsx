
const Products = ({products, isLoading}) => {



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