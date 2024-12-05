'use client';

import './about.css';

function AboutPage() {
    return (
        <div className="about-container">
            <h1 className="about-title">Meet the Developers</h1>
            <p className="about-description">
                TradeSense is an innovative platform designed to revolutionize the cryptocurrency
                trading experience by integrating artificial intelligence. As cryptocurrency continues
                to grow in popularity, many new traders face the daunting challenge of understanding
                market trends and making informed decisions. With the rapid fluctuations in prices, it’s
                easy for newcomers to feel overwhelmed. TradeSense addresses this issue by providing
                AI-driven insights that simplify the trading process. Our machine learning algorithms
                analyze market data and trends to predict price movements and offer real-time
                recommendations to help users make informed decisions. Whether you're new to cryptocurrency
                or an experienced trader, our platform offers tools to lower the barriers to entry, making
                it easier for anyone to start trading confidently. By automating critical processes like market
                analysis and trading actions, TradeSense empowers users to stay ahead of the curve and maximize
                their trading potential without the need for constant manual monitoring.
            </p>
            <p className="key-statement">
                Unlock the power of AI-driven cryptocurrency with TradeSense — 
                <span className="key-statement-bold"> where innovation meets simplicity</span>.
            </p>
            <div className="about-team">
                <div className="about-member">
                    <img src="/user.png" alt="Mathew" /> 
                    <h2 className="about-member-name">Mathew</h2>
                    <p>Full-stack developer with expertise in payment systems.</p>
                </div>
                <div className="about-member">
                    <img src="/user.png" alt="Anthony" />
                    <h2 className="about-member-name">Anthony</h2>
                    <p>Experience in AI research and app development.</p>
                </div>
                <div className="about-member">
                    <img src="/user.png" alt="Tri" /> 
                    <h2 className="about-member-name">Tri</h2>
                    <p>AI department with experience in computer networks.</p>
                </div>
                <div className="about-member">
                    <img src="/user.png" alt="Jasper" /> 
                    <h2 className="about-member-name">Jasper</h2>
                    <p>Experienced in web development and deployment.</p>
                </div>
            </div>
        </div>
    );
}

export default AboutPage;
