// MarketCard.jsx
import React, { useEffect, useState } from 'react';
import Price from './backendCalls/price';
import api from '@/api';

function MarketCard({ crypto, logo }) {
    const [percent, setPercent] = useState(null);

    useEffect(() => {
        const fetchPercentChange = async () => {
            try {
                const response = await api.get(`/percent-change-${crypto}`);
                setPercent(response.data);
            } catch (error) {
                console.error("Error fetching percent change:", error);
            }
        };

        fetchPercentChange();
    }, [crypto]);

    return (
        <div className="market-card">
            <div className="market-card-header">
                <img src={`/${logo}`} alt={crypto} className="crypto-logo" />
            </div>
            <div className="market-card-body">
                <h3 className="market-card-title">{crypto}</h3>
                <Price coin={crypto} />
                <p >

                </p>
            </div>
        </div>
    );
}

export default MarketCard;