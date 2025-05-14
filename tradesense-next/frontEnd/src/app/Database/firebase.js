import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
    apiKey: "AIzaSyDA8J0_v4FdmIW8jkGx33-vDTI7GyNa1vc",
    authDomain: "tradesense195.firebaseapp.com",
    projectId: "tradesense195",
    storageBucket: "tradesense195.firebasestorage.app",
    messagingSenderId: "388322607509",
    appId: "1:388322607509:web:b6b984fc2867696c67f69c",
    measurementId: "G-7XVPLP7HS9"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
const db = getFirestore(app);
export { db };