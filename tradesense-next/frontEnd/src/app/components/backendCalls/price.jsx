import React, { useEffect, useState } from 'react';
import api from '@/api';

const Price = ({ coin }) => {
    const [price, setPrice] = useState(null);
    const [percentChange, setPercentChange] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const priceResponse = await api.get(`/current-price-${coin}`);
                setPrice(priceResponse.data);

                const percentResponse = await api.get(`/percent-change-${coin}`);
                const percent = percentResponse.data;

                // Add "+" if positive
                const formattedPercent = percent > 0 ? `+${percent}%` : `${percent}%`;
                setPercentChange(formattedPercent);
            } catch (error) {
                console.error("Error fetching price data", error);
            }
        };

        fetchData();
    }, [coin]);

    if (price === null || percentChange === null) {
        return <p>Loading...</p>;
    }

    return (
        <>
            <p className="market-card-amount">${price.toLocaleString()}</p>
            <p className={`market-card-percentage ${parseFloat(percentChange) >= 0 ? 'positive' : 'negative'}`}>
                {percentChange}
            </p>
        </>
    );
};

export default Price;