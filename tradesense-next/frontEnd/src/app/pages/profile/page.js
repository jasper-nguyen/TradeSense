'use client';

import React from 'react';
import { useRouter } from 'next/navigation';

function ProfilePage() {
    const router = useRouter();

    const handleLogout = () => {
        localStorage.removeItem('isLoggedIn');
        alert("Logged out!");
        router.push('/');
    };

    return (
        <div style={{ display: 'flex', justifyContent: 'center', marginTop: '100px' }}>
            <button onClick={handleLogout} style={{
                padding: '12px 24px',
                fontSize: '16px',
                backgroundColor: '#dc3545',
                color: 'white',
                border: 'none',
                borderRadius: '5px',
                cursor: 'pointer'
            }}>
                Log Out
            </button>
        </div>
    );
}

export default ProfilePage;