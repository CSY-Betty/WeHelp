// 確認DOM讀取完
document.addEventListener("DOMContentLoaded", function() {
    // 處理刪除留言
    const deleteForms = document.querySelectorAll('.delete-form');

    deleteForms.forEach(function(deleteForm){
        deleteForm.addEventListener("click", function(event) {
            event.preventDefault();
            const confirmed = window.confirm("確定要刪除嗎？");
            if (confirmed) {
                deleteForm.setAttribute("action", `/deleteMessage`);
                deleteForm.method = "POST";
                deleteForm.submit();
            }
        });
    })    
}) 

