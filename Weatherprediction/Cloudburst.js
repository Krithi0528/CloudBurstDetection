import React,{useEffect,useState} from 'react'
import axios from 'axios';
import './Cloudburst.css';
import Burst from './Burst';
export default function Cloudburst() {
  const[data,setData]=useState({
    celcius:10,
    name:'London',
    humidity:10,
    speed: 2,
    image:'https://i.pinimg.com/736x/ff/47/6f/ff476f253a4695d1e499e1e96a5793c1.jpg'
  })
  const [name,setName]=useState('');
  const [error,setError]=useState('');
  const handleClick=()=>{
    if(name !== ""){
      const apiUrl=`https://api.openweathermap.org/data/2.5/weather?q=${name}&appid=a6673e782011461b31f86f49a5d71adb&units=metric`;
      axios.get(apiUrl)
      .then(res=>{
        let imagePath='';  
        if(res.data.weather[0].main=="Clouds"){
          imagePath="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSWK73xsvXugI2Vf_YqiUgxTPx_FyiE1v4tXQ&usqp=CAU"
        }else if(res.data.weather[0].main=="Clear"){
            imagePath="https://w7.pngwing.com/pngs/491/228/png-transparent-cartoon-cloud-animation-clouds-cartoon-blue-white-hand-thumbnail.png"
        }else if(res.data.weather[0].main=="Drizzle"){
          imagePath="https://img.freepik.com/premium-vector/weather-icon-sun-cloud-with-rain-rainy-weather-vector-illustration-isolated_615232-424.jpg"
        }else if(res.data.weather[0].main=="Mist"){
          imagePath="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTQWRnd0sKGUH5Dx9QSqEqWs7pqnJxJQnRZsND7KsaCqeWM7qPgxXDpXevfm5N5uF2VMuI&usqp=CAU"
        }else{
          imagePath="https://i.pinimg.com/736x/ff/47/6f/ff476f253a4695d1e499e1e96a5793c1.jpg"
        }
        setError('');
        console.log(res.data);
        setData({...data,celcius:res.data.main.temp, name:res.data.name, 
          humidity:res.data.main.humidity,speed:res.data.wind.speed,
        image:imagePath})
        
      })
      .catch(err=>{

        if(err.response.status==404){
            setError("Invalid City Name")
        }else{
           setError('');
        }
        console.log(err)
      
      });
    }
  }
  return (
    <div>
    <div className='containerq'>
    
     <div className='weather'>
     <div className='search'>
     <input type="text" placeholder='Enter City Name' onChange={e => setName(e.target.value)}/>
     <button><img src="https://cdn-icons-png.flaticon.com/256/3917/3917132.png" onClick={handleClick}height="30px" width="30px" /></button>
     </div>
     <div className='error'>
     <p>{error}</p>
     </div>
     <div className='winfo'>
     <img src={data.image} width="170px"className='icon'/>
     <h1>{Math.round(data.celcius)}°c</h1>
     <h2>{data.name}</h2>
     <div className='details'>
        <div className='col'>
        <img src="https://static-00.iconduck.com/assets.00/humidity-icon-1024x838-vqbjj1sp.png" height="110px" width="200px"/>
        <div className='humidity'>
        <p>{Math.round(data.humidity)}%</p>
        <p>Humidity</p>
        </div>
        </div>
        <div className='col'>
        <img src="https://clipart-library.com/new_gallery/117-1176381_icon-free-download-animated-wind.png" height="110px" width="200px"/>
        <div className='wind'>
        <p>{Math.round(data.speed)} km/h</p>
        <p>Wind</p>
        </div>
        </div>
     </div>
     </div>
     </div>
     <Burst/>
</div>
</div>
)
}