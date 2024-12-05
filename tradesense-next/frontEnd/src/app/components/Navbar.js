'use client';  

import Link from 'next/link';
import './Navbar.css'; 
function Navbar() {
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
                <Link href="/pages/login"><button className="navbar-button1">Log In</button></Link>
                <Link href="/pages/registration"><button className="navbar-button2">Register</button></Link>
            </div>
        </nav>
    );
}

export default Navbar;
