// cms_django/static/js/form.js
document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("toggle-password");
    const input = document.getElementById("id_password");
  

    // ログイン時のローディング機能
    const loginForm = document.getElementById("login-form");
    const loginBtn = document.getElementById("login-btn");

    if (loginForm && loginBtn) {
      loginForm.addEventListener("submit", function () {
        loginBtn.disabled = true;
        loginBtn.textContent = "ログイン中...";
      });
    }
  });
  