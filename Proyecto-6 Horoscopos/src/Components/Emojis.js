import React, { useEffect } from 'react';
import '../style/Emojis.css';

const Emojis = () => {

    const COUNT = 50;

    const SIZES = [
        'rainDrop--s',
        'rainDrop--s',
        'rainDrop--s',
        // ... otras clases de tamaño
    ];

    const EMOJI = [
        '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑', '♒', '♓', '🔮', '🌙', '🌞', '🌝', '🌛', '🌜', '🌚'
    ];

    useEffect(() => {
        const rainContainer = document.querySelector('.rain-container');

        const genRainDrop = (size, xStart, xEnd, yStart, emoji) => {
            const r = document.createElement('div');
            r.innerText = emoji;
            r.classList.add('rainDrop', size);
            r.style.setProperty('--x-start', xStart + 'vw');
            r.style.setProperty('--x-end', xEnd + 'vw');
            r.style.setProperty('--y-start', yStart + 'vh');
            r.style.setProperty('--y-end', yStart + 200 + 'vh');

            return r;
        }

        for (let i = 0; i < COUNT; i++) {
            const size = randFromList(SIZES);
            const xStart = getRamdomArbitrary(0, 100);
            const xEnd = getRamdomArbitrary(xStart - 20, xStart + 20);
            const emoji = randFromList(EMOJI);
            const yStart = getRamdomArbitrary(-100, 0);

            rainContainer.appendChild(genRainDrop(size, xStart, xEnd, yStart, emoji));
        }
    }, []);

    function randFromList(items) {
        return items[Math.floor(Math.random() * items.length)];
    }

    function getRamdomArbitrary(min, max) {
        return Math.random() * (max - min) + min;
    }

    return (
        <div className="rain-container">        
        </div>
    )
}

export default Emojis;
