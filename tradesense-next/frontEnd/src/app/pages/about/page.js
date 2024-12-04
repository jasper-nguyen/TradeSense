'use client'; 

import './about.css';

function AboutPage() {
    return (
        <div className="about-container">
            <h1 className="about-title">About Us</h1>
            <div className="about-team">
                <div className="about-member">
                    <h2>Mathew</h2>
                    <p>Full-stack developer with expertise in payment systems.</p>
                </div>
                <div className="about-member">
                    <h2>Anthony</h2>
                    <p>Experience in AI research and app development.</p>
                </div>
                <div className="about-member">
                    <h2>Tri</h2>
                    <p>AI department at my company, with experience in computer networks.</p>
                </div>
                <div className="about-member">
                    <h2>Jasper</h2>
                    <p>Experienced in web development.</p>
                </div>
            </div>
        </div>
    );
}

export default AboutPage;
