'use client';

import React, { useState } from 'react';
import '../info.css';
import InfoCard from '@/app/components/backendCalls/infoCard';

function ETHPage({ crypto }) {
    crypto = "ETH";
    return (
        <div className="crypto-container">
            <h2 className="crypto-title">{crypto}</h2>
            <InfoCard coin={crypto} />
        </div>
    );
}

export default ETHPage;
