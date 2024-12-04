'use client'; // Mark as client component

import Navbar from './components/Navbar.js'; // Import the Navbar
import Footer from './components/Footer.js'; // Import the Footer
import './globals.css'; 

function Layout({ children }) {
    return (
        <>
            <html lang="en">
                <head>
                    <meta charSet="UTF-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <title>TradeSense</title>
                    <link rel="icon" href="/homelogo.png" type="image/png" />
                </head>
                <body>
                    {/* Include the Navbar at the top of every page */}
                    <Navbar />
                    <main>
                        {children}
                    </main>
                    <Footer />
                </body>
            </html>
        </>
    );
}

export default Layout;
