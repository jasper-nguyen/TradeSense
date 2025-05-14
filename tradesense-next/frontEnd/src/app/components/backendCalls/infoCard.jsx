import React, { useEffect, useState } from 'react';
import api from '@/api';
import './infoCard.css'

const InfoCard = ({ coin }) => {
    const [info, setInfo] = useState([]);

    const fetchInfo = async () => {
        try {
            let infoCall = `/info-${coin}`;
            const response = await api.get(infoCall);
            setInfo(response.data);

        } catch (error) {
            console.error("Error fetching info", error);
        }
    };

    useEffect(() => {
        fetchInfo();
    }, []);

    return (
        <div className="crypto-card">
            <ul className="crypto-list">
                {info.map(item => {
                    return <li key={item.id}>{item}</li>;
                })}
            </ul>
        </div>
    );
};

export default InfoCard;