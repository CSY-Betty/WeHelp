// 確認DOM讀取完
document.addEventListener("DOMContentLoaded", function() {
    // 處理會員姓名查詢
    const usernameButton = document.getElementById("usernameSubmit")
    const searchResult = document.getElementById("searchResult");
    
    usernameButton.addEventListener("click", function(event) {
        event.preventDefault();

        const usernameInput = document.getElementById("usernameInput");
        const usernameText = usernameInput.value;

        if (usernameText) {
            fetch(`/api/member?username=${usernameText}`, {
                method: "GET",
                headers: {
                    "Content-Type": "application/json",
                },
            })
            .then(respose => respose.json())
            .then(data => {
                if(data.data) {
                    nameSearch = data.data.name,
                    usernameSearch = data.data.username
    
                    searchResult.textContent = `${nameSearch}(${usernameSearch})`;
                }
                else {
                    searchResult.textContent = "無此會員";
                }
            })
            .catch(error => {
                console.error("An error occurred:", error);
            });
        }
    })

    // 處理姓名修改
    const newnameButton = document.getElementById("newnameSubmit")

    newnameButton.addEventListener("click", function(event){
        event.preventDefault();

        const newnameInput = document.getElementById("newname");
        const newnamechange = document.getElementById("newnamechange");
        const defaultname = document.getElementById("defaultname");

        const newnameText = newnameInput.value;

        if (newnameText) {
            const requestData = {
                "name":newnameText
            }
            fetch("/api/member", {
                method: "PATCH",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(requestData)
            })
            .then(respose => respose.json())
            .then(data => {
                if (data.ok) {
                    defaultname.textContent = `${newnameText}，歡迎登入系統`;
                    newnamechange.textContent = "更新成功";
                } else {
                    console.error("Update failed");
                }
            })
            .catch(error => {
                console.error("An error occurred:", error);
            });
        }


    })



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


