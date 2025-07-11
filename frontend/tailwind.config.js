// tailwind.config.js
const { fontFamily } = require('tailwindcss/defaultTheme');

module.exports = {
  content: [
    './app/**/*.{js,jsx,ts,tsx}',
    './components/**/*.{js,jsx,ts,tsx}',
    './screens/**/*.{js,jsx,ts,tsx}',
  ],
  presets: [require('nativewind/preset')],
  theme: {
    extend: {
      fontFamily: {
        // Añadimos Poppins
        poppins: ['Poppins_400Regular', ...fontFamily.sans],
        poppinsBold: ['Poppins_700Bold', ...fontFamily.sans],
      },
      colors: {
        primary1: '#0077B6',
        primary2: '#00B4D8',
      },
      backgroundImage: {
        'main-gradient': 'linear-gradient(to bottom, #0077B6, #00B4D8)',
      },
    },
  },
  plugins: [],
};
