// suggestionPopup.jsx
import React, { useState } from 'react';
import api from '@/api';
import './popup.css';

// your existing Popup
function Popup({ trigger, setTrigger, children }) {
    return trigger ? (
        <div className="popup">
            <div className="popup-inner">
                <button className="close-btn" onClick={() => setTrigger(false)}>
                    close
                </button>
                {children}
            </div>
        </div>
    ) : null;
}


export default function SuggestionPopup({ coin = 'BTC' }) {
    const [trigger,  setTrigger]  = useState(false);
    const [rawData,  setRawData]  = useState('');
    const [message,  setMessage]  = useState('');

    const handleSuggest = async () => {
        try {
            // call the correct endpoint for this coin
            const { data: raw } = await api.get(`/evaluate-${coin.toUpperCase()}`);
            setRawData(raw);

            const m = raw.match(/'(decreased|increased)'/);
            if (!m) throw new Error('No direction found in response');

            setMessage(m[1] === 'decreased' ? 'SELL' : 'BUY');
        } catch (err) {
            console.error(err);
            setRawData('');
            setMessage('Error fetching suggestion');
        } finally {
            setTrigger(true);
        }
    };

    return (
        <>
            <button
                className="suggest-button"
                onClick={handleSuggest}
            >
                Suggest
            </button>

            <Popup trigger={trigger} setTrigger={setTrigger}>
                <div style={{ textAlign: 'center', padding: '2rem' }}>
                    {rawData && (
                        <>
                            <h4>Full response:</h4>
                            <pre style={{
                                textAlign: 'left',
                                background: '#f5f5f5',
                                padding: '1rem',
                                borderRadius: '4px',
                                overflowX: 'auto'
                            }}>
                {rawData}
              </pre>
                        </>
                    )}
                    <h2 style={{ marginTop: '1.5rem' }}>{message}</h2>
                </div>
            </Popup>
        </>
    );
}