import React, { useState } from 'react';
import function_check from '../Functions/function_check';
import function_horosco from '../Functions/function_horos';
import { AiOutlineWhatsApp } from 'react-icons/ai';
import { BiArrowToLeft } from 'react-icons/bi';
import function_window from '../Functions/function_window';

const Main = () => {
  const [signe, setSigne] = useState('');
  const [horoscope, setHoroscope] = useState('');
  const [mirador, setMirador] = useState(false);
  const [animationSpeed, setAnimationSpeed] = useState(50); // Ajusta la velocidad según tu preferencia
  const [animation, setAnimation] = useState(false); // Ajusta la velocidad según tu preferencia
  const [whatsapp, setWhatsapp] = useState(''); // Ajusta la velocidad según tu preferencia

  const handleSubmit = (e) => {
    e.preventDefault();
    function_horosco(setHoroscope, signe, animationSpeed);
  };

  const handleSubmit2 = (e) => {
      e.preventDefault();
      function_window(setAnimation);    
  };

  const handleSubmit3 = (e) => {
    e.preventDefault();
    function_window(setAnimation);
    const encodedMessage = encodeURIComponent(horoscope);
    const whatsappLink = `https://wa.me/${whatsapp}?text=${encodedMessage}`;
    window.open(whatsappLink, '_blank');
      setAnimation(false);
  };
    


  const function_windowoff = () => {
    setAnimation(false);
  };

  return (
   <>
    {animation ? 
    <>
   <div className='section_whatsapp'>
      <div className='icon_back'onClick={function_windowoff}>
        <BiArrowToLeft />
      </div>
      <div className='form_whatssapp'>
        <form className='form_pedejo' onSubmit={handleSubmit3}>
              <input className='input_horoscopo' placeholder="telefono ? 👈🏻"  type="text" onChange={(e) => setSigne(e.target.value)}/>
            <div className='buttons-container'>
              <button type="submit">Enviar</button>
            </div>
          </form>
      </div>

    </div>
    </>
  :
  <div className='Section_Horoscopo'>
   
    <div className='title_horoscopo'>
      <h1>Bienvenido a tu Horóscopo Negro</h1>
    </div>
    <div className='body_horoscopo'>
        <div className='descrip_horoscopo'>
          <h2>Ingresa tu Horoscopo: </h2>
        </div>
      <div className='form_horoscopo'>
          <form className='form_pedejo' onSubmit={handleSubmit}>
              <input className='input_horoscopo' onFocus={() => function_check(setMirador)} placeholder={mirador ? "..." :"¿Horoscopo? 👈🏻"} name="text" type="text" value={signe} onChange={(e) => setSigne(e.target.value)}/>
            <div className='buttons-container'>
              <button type="submit">Obtener Horóscopo</button>
              {horoscope ? 
              <div className='button-whatsapp' onClick={handleSubmit2}>
              <AiOutlineWhatsApp  className='scale-up-ver-bottom' /> 
              </div>
              :
              ""  
              }
              
              
            </div>
          </form>
      </div>
    </div>
      {horoscope ?  
      <div className='parameter_horosc'>
          <h1>{horoscope}</h1>
      </div>
     :
      ""   
  }

  </div>
  }
    </>
  );
};

export default Main;
