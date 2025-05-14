'use client';  // Mark as client component

import { db } from "../../Database/firebase";
import { useRouter } from 'next/navigation';
import { collection, addDoc, query, where, getDocs } from "firebase/firestore";
import React, { useState } from 'react';
import './login.css'; 

function LoginPage() {
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const router = useRouter();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const usersRef = collection(db, "users");
            const q = query(usersRef, where("email", "==", formData.email));
            const querySnapshot = await getDocs(q);

            if (!querySnapshot.empty) {
                const userDoc = querySnapshot.docs[0];
                const userData = userDoc.data();

                if (userData.password === formData.password) {
                    // ✅ Success
                    localStorage.setItem("isLoggedIn", "true");
                    alert("Login successful!");
                    router.push("/pages/market");
                } else {
                    alert("Incorrect password");
                }
            } else {
                alert("No user found with this email");
            }
        } catch (error) {
            console.error("Login error:", error);
            alert("Something went wrong. Check console.");
        }
    };

    return (
        <div className="login-container">
            <h2 className="login-title">Login to Your Account</h2>
            <h3 className="login-subtitle">Welcome Back!</h3>
            <div className="login-box">
                
                <form onSubmit={handleSubmit}>
                    <div className="input-group">
                        <label htmlFor="email">Email Address</label>
                        <input
                            type="email"
                            id="email"
                            name="email"
                            value={formData.email}
                            onChange={handleChange}
                            required
                            placeholder="email@domain.com"
                        />
                    </div>
                    <div className="input-group">
                        <label htmlFor="password">Password</label>
                        <input
                            type="password"
                            id="password"
                            name="password"
                            value={formData.password}
                            onChange={handleChange}
                            required
                            placeholder="********"
                        />
                    </div>
                    <button type="submit" className="submit-button">Login</button>
                </form>
            </div>
        </div>
    );
}

export default LoginPage;
