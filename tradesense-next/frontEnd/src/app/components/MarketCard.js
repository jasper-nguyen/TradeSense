import React from 'react';
import Image from 'next/image';
import Price from './backendCalls/price';

function MarketCard({ crypto, logo, percentage }) {
    return (
        <div className="market-card">
            <div className="market-card-header">
                <img src={`/${logo}`} alt={crypto} className="crypto-logo" />
            </div>
            <div className="market-card-body">
                <h3 className="market-card-title">{crypto}</h3>
                <Price coin={crypto} />
                <p className={`market-card-percentage ${percentage.startsWith('+') ? 'positive' : 'negative'}`}>
                    {percentage}
                </p>
            </div>
        </div>
    );
}

export default MarketCard;
