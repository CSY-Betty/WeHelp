// 確認DOM讀取完
document.addEventListener("DOMContentLoaded", function() {
  
    // 處理登入問題
    const loginButton = document.querySelector('input[name="submit"]');
    loginButton.addEventListener("click", function(event) {
    const agreeCheckbox = document.querySelector('input[name="agree"]');

    if (!agreeCheckbox.checked) {
        event.preventDefault();
        alert("Please check the checkbox first!");
    }
    });

	// 處理calculate
    const calculateForm = document.querySelector('form[name="calculate"]');
    calculateForm.addEventListener("submit", function(event) {
    event.preventDefault();
    positiveInput = document.querySelector('input[name="positive"]');
    const inputValue = positiveInput.value.trim();

    // 判斷是否為正整數
    if (isPositiveInteger(inputValue)) {
        calculateForm.setAttribute("action", `/square/${inputValue}`);
        calculateForm.method = "POST";
        calculateForm.submit();
    } else {
        alert("Please enter a positive number.");
    }
    });
}) 

function isPositiveInteger(value) {
	const numValue = Number(value);
	return Number.isInteger(numValue) && numValue >= 0;
}
