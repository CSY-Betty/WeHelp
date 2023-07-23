// 建立照片模板
function createAndAppendElementPic(tag, className, src, container) {
    const element = document.createElement(tag);
    element.classList.add(className);    
    const img = document.createElement("img");
    img.src = src;
    element.appendChild(img);
    
    container.appendChild(element)
}

// 建立景點名稱模板
function createAndAppendElementText(tag, className, title, container) {
    const element = document.createElement(tag);
    element.classList.add(className);
    element.textContent = title;
    container.appendChild(element)
}

// 處理取得的資料並套入模板
function processDataAndDisplay(data, isProduct){
    data.forEach(function(item) {
        const {file, stitle} = item;
        // 取得圖片的第一個網址
        let file_lower = file.toLowerCase();
        const image = file_lower.indexOf(".jpg");
        const first_image = file.substring(0, image + 4);

        // 建立最外層區塊
        if (isProduct) {
            const container = document.getElementById("product-container")
            const productItem = document.createElement("div");
            productItem.classList.add("product-item");

            createAndAppendElementPic("div", "attractionPic", first_image, productItem)
            createAndAppendElementText("div", "attractionName", stitle, productItem)

            container.appendChild(productItem)
        }
        else {
            const container = document.getElementById("attractions-container")
            const titleItem = document.createElement("div");
            titleItem.classList.add("title-item");

            createAndAppendElementPic("div", "attractionPic", first_image, titleItem)
            createAndAppendElementPic("div", "star", "./star.png", titleItem)
            createAndAppendElementText("div", "attractionName", stitle, titleItem)
            

            container.appendChild(titleItem);
        }
        
    })

}


// 爬取資料
fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
    .then(response => response.json())
    .then(function(responseData) {
        const productData = responseData.result.results.slice(0,3);
        const articleData = responseData.result.results.slice(3,15);
        processDataAndDisplay(productData, true);
        processDataAndDisplay(articleData, false);
    })
    

// 設定load more按鈕
let currentIndex = 15;
const totalAttractions = 58;
const loadMoreButton = document.getElementById("load-more");
loadMoreButton.addEventListener("click", function() {
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json")
    .then(response => response.json())
    .then(function(responseData) {
        data = responseData.result.results;
        const endIndex = Math.min(currentIndex + 12, totalAttractions);
        articleData = data.slice(currentIndex, endIndex);
    
        if (articleData.length >= 12) {
            processDataAndDisplay(articleData, false);
            currentIndex = endIndex;

            if (currentIndex === totalAttractions) {
                loadMoreButton.disabled = true;
            }
        }
        else {
            const articleData = data.slice(currentIndex);
            processDataAndDisplay(articleData, false);
            loadMoreButton.disabled = true;
        }
    })
})
