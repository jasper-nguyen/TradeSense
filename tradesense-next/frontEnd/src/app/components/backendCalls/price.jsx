import React, { useEffect, useState } from 'react';
import api from '@/api';

const Price = ({ coin }) => {
    const [price, setPrice] = useState([]);

    const fetchPrice = async () => {
        try {
            let priceCall = `/current-price-${coin}`;
            const response = await api.get(priceCall);
            setPrice(response.data);
        } catch (error) {
            console.error("Error fetching price", error);
        }
    };

    useEffect(() => {
        fetchPrice();
    }, []);

    return (
        <p className="market-card-amount">{price}</p>
    );
};

export default Price;