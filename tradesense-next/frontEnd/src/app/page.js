import React from 'react';
import Link from 'next/link';
import './main.css';

function HomePage() {
    return (
        <div className="homepage-container">
            {/* Hero Section */}
            <section className="hero-section">
                <div className="hero-content">
                    <h1 className="hero-title">Welcome to TradeSense</h1>
                    <p className="hero-description">
                        Unlock the power of AI to make smarter cryptocurrency trades. 
                        Our AI-enhanced platform analyzes trends, predicts prices, and 
                        automates trading to maximize YOUR profits.
                    </p>
                    <Link href="/pages/registration"> 
                        <button className="cta-button">Get Started</button>
                    </Link>
                </div>
            </section>

            {/* Features Section */}
            <section className="features-section">
                <div className="feature">
                    <h2 className="feature-title">AI-Driven Predictions</h2>
                    <p className="feature-description">
                        Our AI models predict cryptocurrency price movements, helping you make informed decisions about when to buy and sell.
                    </p>
                </div>
                <div className="feature">
                    <h2 className="feature-title">Real-Time Market Data</h2>
                    <p className="feature-description">
                        Stay up-to-date with real-time tracking of all major cryptocurrencies. Monitor trends and prices with ease.
                    </p>
                </div>
                <div className="feature">
                    <h2 className="feature-title">Automated Trading</h2>
                    <p className="feature-description">
                        Let the platform automate your trades based on AI analysis. Never miss a trading opportunity again.
                    </p>
                </div>
            </section>

            {/* Sign-Up Section */}
            <section className="signup-section">
                <h2 className="signup-title">Start Trading Today</h2>
                <p className="signup-description">Join thousands of successful traders using TradeSense to make smarter trades with the help of AI.</p>
                <button className="cta-button">Sign Up</button>
            </section>

            {/* Footer Section */}
            <footer className="footer">
                <div className="footer-content">
                    <p>&copy; 2024 TradeSense. All Rights Reserved.</p>
                    <div className="footer-links">
                        <a href="/about">About Us</a>
                        <a href="/contact">Contact</a>
                        <a href="/privacy">Privacy Policy</a>
                    </div>
                </div>
            </footer>
        </div>
    );
}

export default HomePage;
