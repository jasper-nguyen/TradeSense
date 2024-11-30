import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:5000", // Update this to your backend's URL
  headers: {
    "Content-Type": "application/json",
  },
});

export default apiClient;
