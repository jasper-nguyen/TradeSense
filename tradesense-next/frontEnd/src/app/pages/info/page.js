'use client';

import React, { useState } from 'react';
import './info.css';

function MarketPage() {
    const [filter, setFilter] = useState('Trade Volume');  // Default filter
    let time = new Date();
    let high = 618.35;
    let low = 613.01;
    let open = 617.65;
    let close = 615.77;
    let volumefrom = 13430.26;
    let volumeto = 8320759.40;
    return (
        <div className="crypto-container">
            <h2 className="crypto-title">BTC/USD (Last Minute)</h2>
            <div className="crypto-card">
                <ul className="crypto-list">
                    <li><span>Time:</span> {new Date(time).toLocaleString()}</li>
                    <li><span>Open:</span> ${open}</li>
                    <li><span>High:</span> ${high}</li>
                    <li><span>Low:</span> ${low}</li>
                    <li><span>Close:</span> ${close}</li>
                    <li><span>Volume From:</span> {volumefrom}</li>
                    <li><span>Volume To:</span> {volumeto}</li>
                </ul>
            </div>
        </div>
    );
}

export default MarketPage;
