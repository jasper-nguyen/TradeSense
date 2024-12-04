'use client'; // Mark as client component

import Navbar from './components/Navbar'; // Import the Navbar
import './globals.css'; // Link to global styles (if needed)

function Layout({ children }) {
    return (
        <>
            {/* HTML and Body structure for the page */}
            <html lang="en">
                <head>
                    {/* Add any meta tags, title, or favicon */}
                    <meta charSet="UTF-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <title>TradeSense - AI-Enhanced Crypto Trading</title>
                    {/* You can add any other global tags here */}
                </head>
                <body>
                    {/* Include the Navbar at the top of every page */}
                    <Navbar />
                    <main>
                        {/* Render the page-specific content below the Navbar */}
                        {children}
                    </main>
                </body>
            </html>
        </>
    );
}

export default Layout;
