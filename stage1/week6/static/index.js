// 確認DOM讀取完
document.addEventListener("DOMContentLoaded", function() {
    // 處理註冊問題
    const registerButton = document.querySelector('input[name="register"]');
    registerButton.addEventListener("click", function(event) {
        let nameCheck = document.querySelector('form[name="registerForm"] input[name="name"]');
        let usernameCheck = document.querySelector('form[name="registerForm"] input[name="username"]');
        let passwordCheck = document.querySelector('form[name="registerForm"] input[name="password"]');

        // 檢查姓名欄位是否有輸入資訊
        if (nameCheck.value.trim() === "") {
            alert("Please enter your name.");
            event.preventDefault();
        };

        // 檢查帳號欄位是否有輸入資訊
        if (usernameCheck.value.trim() === "") {
            alert("Please enter your username.");
            event.preventDefault();
        };

        // 檢查密碼欄位是否有輸入資訊
        if (passwordCheck.value.trim() === "") {
            alert("Please enter your password.");
            event.preventDefault();
        };
    });

    // 處理登入問題
    const loginButton = document.querySelector('input[name="submit"]');
    loginButton.addEventListener("click", function(event) {
        let usernameCheck = document.querySelector('form[name="signinForm"] input[name="username"]');
        let passwordCheck = document.querySelector('form[name="signinForm"] input[name="password"]');

        // 檢查帳號欄位是否有輸入資訊
        if (usernameCheck.value.trim() === "") {
            alert("Please enter your username.");
            event.preventDefault();
        };

        // 檢查密碼欄位是否有輸入資訊
        if (passwordCheck.value.trim() === "") {
            alert("Please enter your password.");
            event.preventDefault();
        };
    });
}) 
