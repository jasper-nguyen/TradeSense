import React, { useEffect, useState } from 'react';
import api from '@/api';

const Price = ({ coin, view }) => {
    const [price, setPrice] = useState(null);
    const [percentChange, setPercentChange] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                // Get current price
                const priceRes = await api.get(`/current-price-${coin}`);
                setPrice(priceRes.data);

                // Determine the correct route based on view
                let percentRoute = '';
                switch (view?.toLowerCase()) {
                    case 'week':
                        percentRoute = `/percent-change-weekly-${coin}`;
                        break;
                    case 'month':
                        percentRoute = `/percent-change-monthly-${coin}`;
                        break;
                    case 'year':
                        percentRoute = `/percent-change-yearly-${coin}`;
                        break;
                    default:
                        percentRoute = `/percent-change-${coin}`; // 24h
                }

                // Get percent change
                const percentRes = await api.get(percentRoute);
                const percent = percentRes.data;
                const formatted = percent > 0 ? `+${percent}%` : `${percent}%`;
                setPercentChange(formatted);
            } catch (err) {
                console.error("Error fetching price or percent change", err);
            }
        };

        fetchData();
    }, [coin, view]);

    if (price === null || percentChange === null) {
        return <p>Loading...</p>;
    }

    return (
        <>
            <p className="market-card-amount">${price.toLocaleString()}</p>
            <p className={`market-card-percentage ${parseFloat(percentChange) >= 0 ? 'positive' : 'negative'}`}>
                {percentChange} over {view}
            </p>
        </>
    );
};

export default Price;