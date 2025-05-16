'use client';

import React, { useState } from 'react';
import Price from '@/app/components/backendCalls/price';
import '../info.css';
import InfoCard from '@/app/components/backendCalls/infoCard';
import Popup from '@/app/components/backendCalls/suggestionPopup';

let crypto = "BTC"
function BTCPage() {
    const [buttonPopup, setButtonPopup] = useState(false);
    const [view, setView] = useState('Week');

    return (
        <div className="crypto-container">
            <div className="crypto-header">
                <h2 className="crypto-title">Bitcoin price USD</h2>
                <h1 className="crypto-price"><Price coin={crypto} /></h1>
                <p className="crypto-change">+20% over 3 months</p>
                <select className="time-select" value={view} onChange={(e) => setView(e.target.value)}>
                    <option value="Week">Week</option>
                    <option value="Month">Month</option>
                    <option value="Year">Year</option>
                </select>
                <button onClick={() => setButtonPopup(true)} className="suggest-button">Suggest</button>
                <Popup trigger={buttonPopup} setTrigger={setButtonPopup}>
                    <h3>My Popup</h3>
                    <p>This is my button popup</p>
                </Popup>
            </div>

            <div className="crypto-history">
                <h3>Price history</h3>
                <h2 className="crypto-title">{crypto}</h2>
                <InfoCard coin={crypto} />

            </div>

            <div className="crypto-prices">
                <div className="price-card">
                    <h4>Bitcoin</h4>
                    <p>$45,678.90</p>
                    <p>+20% over 3 months</p>
                </div>
                <div className="price-card">
                    <h4>Ethereum</h4>
                    <p>$2,405</p>
                    <p>+33% over 5 months</p>
                </div>
                <div className="price-card">
                    <h4>XRP</h4>
                    <p>$2.63</p>
                    <p>+86% over 1 month</p>
                </div>
            </div>
        </div>
    );
}

export default BTCPage;