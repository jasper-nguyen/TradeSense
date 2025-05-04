'use client';
import React, { useState } from 'react';
import './registration.css';
import Link from 'next/link';
import { db } from "../../Database/firebase";
import { collection, addDoc } from "firebase/firestore";
import { useRouter } from 'next/navigation';

function RegistrationPage() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        confirmPassword: ''
    });


    const router = useRouter();

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value
        });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log("Form submitted:", formData);

        try {
            console.log("Attempting to add to Firestore...");
            await addDoc(collection(db, "users"), {
                name: formData.name,
                email: formData.email,
                password: formData.password,
            });
            console.log("Added!");

            alert("User registered successfully!");
            setFormData({ name: '', email: '', password: '', confirmPassword: '' });

            setFormData({
                name: '',
                email: '',
                password: '',
                confirmPassword: '',
            });
            router.push('/pages/login');
        } catch (error) {
            console.error("Error adding user to Firestore:", error);
            alert("Registration failed. Check the console.");
        }
    };


    return (
        <div className="registration-container">
            <h2 className="registration-title">Create an Account</h2>
            <h3 className="registration-subtitle">Enter Your Details to Start Trading</h3>
            <div className="registration-box">
                <form onSubmit={handleSubmit}>
                    <div className="input-group">
                        <label htmlFor="name">Full Name</label>
                        <input
                            type="text"
                            id="name"
                            name="name"
                            value={formData.name}
                            onChange={handleChange}
                            required
                            placeholder="John Doe"
                        />
                    </div>
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
                    <div className="input-group">
                        <label htmlFor="confirmPassword">Confirm Password</label>
                        <input
                            type="password"
                            id="confirmPassword"
                            name="confirmPassword"
                            value={formData.confirmPassword}
                            onChange={handleChange}
                            required
                            placeholder="********"
                        />
                    </div>
                    <button type="submit" className="submit-button">Continue</button>
                </form>
            </div>
        </div>
    );
}

export default RegistrationPage;

