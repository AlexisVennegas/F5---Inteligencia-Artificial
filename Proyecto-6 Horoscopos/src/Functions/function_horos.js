import mentadaData from "../json/mentada.json";


const function_horosco = (setHoroscope, canSelectHoroscope, speed) => {

    if (!canSelectHoroscope) return;
    


    const signos = ["aries", "tauro", "geminis", "cancer", "leo", "virgo", "libra", "escorpio", "sagitario", "capricornio", "acuario", "piscis"];
    const selectedSign = canSelectHoroscope.toLowerCase();
    if (!signos.includes(selectedSign)) {
        setHoroscope("Signo inválido");
        return;
    }
    const randomIndex = Math.floor(Math.random() * mentadaData.length);
    const randomHoroscope = mentadaData[randomIndex].mentadata;

    if (randomHoroscope) {
        const characters = randomHoroscope.split("");
        let animatedText = '';

        characters.forEach((char, index) => {
            setTimeout(() => {
              animatedText += char;
              setHoroscope(canSelectHoroscope +  ', ' + animatedText);
            }, index * speed);
        });      
    } else {
      setHoroscope("No has ingresado tu Horóscopo");
    }

    
  };

export default function_horosco;