/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./templates/**/*.html",
      "./blog/templates/**/*.html",
      "./cms_django/templates/**/*.html",    // ← これをアンコメント or 追加
    ],
    theme: { 
      extend: {
        animation: {
          'fade-in': 'fadeIn 0.8s ease-out',
        },
        keyframes: {
          fadeIn: {
            '0%': { opacity: '0', transform: 'scale(0.95)' },
            '100%': { opacity: '1', transform: 'scale(1)' },
          },
        },
        backgroundImage: {
          'login-bg': "url('/static/css/img/bg.jpg')",
        }
      } 
    },
    plugins: [],
  }
  
  