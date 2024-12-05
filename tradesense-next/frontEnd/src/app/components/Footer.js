import React from 'react';
import './Footer.css';  

const Footer = () => {
  return (
    <footer className="footer">
      <div className="footer-content">
        <p>&copy; 2024 TradeSense. All Rights Reserved.</p>
        <div className="footer-links">
          <a 
            href="https://github.com/definetlynottri/Cmpe195a" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            About Us
          </a>

          <a 
            href="https://github.com/definetlynottri/Cmpe195a" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Contact
          </a>

          <a 
            href="https://github.com/definetlynottri/Cmpe195a" 
            target="_blank" 
            rel="noopener noreferrer"
          >
            Privacy Policy
          </a>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
