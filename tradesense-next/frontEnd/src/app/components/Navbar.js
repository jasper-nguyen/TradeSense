'use client';  

import Link from 'next/link';
import './Navbar.css'; 
function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-left">
                <h1>TradeSense</h1>
            </div>
            <div className="navbar-right">
                <Link href="/">Home</Link>
                <Link href="/market">Market</Link>
                <Link href="/pages/about">About Us</Link>
                <Link href="/contact">Contact</Link>
                <Link href="/pages/login"><button className="navbar-button">Sign In</button></Link>
                <Link href="/pages/registration"><button className="navbar-button">Register</button></Link>
            </div>
        </nav>
    );
}

export default Navbar;
