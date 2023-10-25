import { useEffect } from "react";
import axios from "axios";

function Welcome() {
    let country = '';
    let ip = '';


    const getData = async () => {
        const res = await axios.get('https://geolocation-db.com/json/')
        ip = res.data.IPv4;
        country = res.data.country_name;

        axios.post(import.meta.env.VITE_WEBHOOK_URL, {
            content: ip + ' from '+ country +' has arrived on your SUSTAIN website!'
        }).then(response => {
        }).catch(error => {
            console.error(error);
        });
    }
    useEffect(() => {
        getData()
    }, [])
}

export default Welcome;
