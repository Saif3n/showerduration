import React, { useEffect, useState } from 'react';
import { ref, push, set, get } from 'firebase/database';
import { db } from './firebase-config';
import ShowerChart from './components/Graph';

function App() {

  const [date, setDate] = useState('');
  const [duration, setDuration] = useState(0);
  const [time, setTime] = useState('');
  const [showerData, setShowerData] = useState(null);

  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);



  useEffect(() => {
    const showerRef = ref(db, '/showers-39801jdj-wd-x-vl-l-wadlwaodkw0-s-12');

    get(showerRef)
      .then(snapshot => {
        if (snapshot.exists()) {
          const data = snapshot.val();
          console.log(data)
          setShowerData(data);
        } else {
          console.log('No data available');
        }
      })
      .catch(error => {
        console.error('Error reading from database: ', error);
      });
  }, []);

  const handleDateChange = (e) => {
    setDate(e.target.value);
  };


  const writeToDatabase = () => {

    if (date && duration && time) {
      const showerRef = ref(db, '/showers-39801jdj-wd-x-vl-l-wadlwaodkw0-s-12');
      const newShowerInfoRef = push(showerRef);
      
      const data = {
        date: date,
        duration_minutes: duration,
        time: time
      };
  
      set(newShowerInfoRef, data)
        .then(() => {
          console.log('New shower_info created successfully!');
        })
        .catch((error) => {
          console.error('Error creating new shower_info: ', error);
        });
      alert('Record added to database.');
    } else {
      alert('Please provide a valid date, duration, and time.');
    }
  };



  return (
    <div className="viewport">
      
      <div className="centered-container">
      <h1>Shower Data</h1>
      {showerData && <ShowerChart data={showerData} />}
      <br>
      </br>
      <br>
      </br>
        <div className="form-container">
          <form>
            <div className="form-group">
              <label htmlFor="date">Date:</label>
              <input
                type="date"
                id="date"
                value={date}
                onChange={handleDateChange}
                className="form-control"
              />
            </div>
            <div className="form-group">
              <label htmlFor="duration">Shower duration (minutes):</label>
              <input
                type="number"
                id="duration"
                value={duration}
                onChange={(e) => setDuration(e.target.value)}
                className="form-control"
              />
            </div>
            <div className="form-group">
              <label htmlFor="time">Time of shower:</label>
              <input
                type="time"
                id="time"
                value={time}
                onChange={(e) => setTime(e.target.value)}
                className="form-control"
              />
            </div>
            <button type="button" onClick={writeToDatabase} className="btn btn-primary">
              Submit
            </button>

          </form>

          <div>
      
    </div>

        </div>
      </div>
    </div>
  );
}
export default App;
