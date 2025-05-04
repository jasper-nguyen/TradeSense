'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import './Navbar.css';

function Navbar() {
    const [isLoggedIn, setIsLoggedIn] = useState(false);

    useEffect(() => {
        const checkLogin = () => {
            const loggedIn = localStorage.getItem('isLoggedIn');
            setIsLoggedIn(loggedIn === 'true');
        };

        checkLogin(); // Initial check

        // 👇 Listen for changes to localStorage (even across tabs)
        window.addEventListener('storage', checkLogin);

        // Optional: recheck on focus (helps when coming back to page)
        window.addEventListener('focus', checkLogin);

        return () => {
            window.removeEventListener('storage', checkLogin);
            window.removeEventListener('focus', checkLogin);
        };
    }, []);

    return (
        <nav className="navbar">
            <div className="navbar-left">
                <div className="navbar-logo">
                    <img src="/homelogo.png" alt="Home Logo" className="logo" />
                    <span className="navbar-title">TradeSense</span>
                </div>
            </div>
            <div className="navbar-right">
                <Link href="/">Home</Link>
                <Link href="/pages/market">Market</Link>
                <Link href="/pages/about">About Us</Link>
                <Link href="https://github.com/definetlynottri/Cmpe195a">Contact</Link>

                {isLoggedIn ? (
                    <Link href="/pages/profile"><button className="navbar-button1">Profile</button></Link>
                ) : (
                    <>
                        <Link href="/pages/login"><button className="navbar-button1">Log In</button></Link>
                        <Link href="/pages/registration"><button className="navbar-button2">Register</button></Link>
                    </>
                )}
            </div>
        </nav>
    );
}

export default Navbar;