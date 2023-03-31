/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        bgblack: "#1F1F1F",
        bglight: "#969593",
        primary: "#E3FFA8",
        olive: "#45ffbc",
      },
      fontFamily: {
        vietnam: ["Be Vietnam Pro", "sans-serif"]},
    },
  },
  plugins: [],
}
