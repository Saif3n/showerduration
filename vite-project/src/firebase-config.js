// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

import { getDatabase } from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDLapiDLZAlTb_n0UlkCP34kQkMQ1zid8Y",
  authDomain: "showerduration.firebaseapp.com",
  databaseURL: "https://showerduration-default-rtdb.firebaseio.com",
  projectId: "showerduration",
  storageBucket: "showerduration.appspot.com",
  messagingSenderId: "132082105578",
  appId: "1:132082105578:web:b3ab1f01fd46b2164eab93",
  measurementId: "G-DBFTEX85T6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getDatabase(app);