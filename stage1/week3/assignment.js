fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json").then(function(response){
    return response.json();
}).then(function(responseData){
    data = responseData.result.results;
    const imageContainer = document.getElementsByClassName("attractionPic");
    const spanContainer = document.getElementsByClassName("attractionName");

    Array.from(imageContainer).forEach(function(container, index) {if (index < data.length){
        const item = data[index];
        const file = item.file;
        const file_lower = file.toLowerCase();
        const image = file_lower.indexOf(".jpg");
        const first_image = file.substring(0, image + 4);
        
        const newImage = document.createElement("img");
        newImage.src = first_image;
        container.appendChild(newImage);
    }});

    Array.from(spanContainer).forEach(function(container, index) {if (index < data.length){
        const item = data[index];
        const stitle = item.stitle;

        const attractionName = document.createElement("span");
        attractionName.textContent = stitle;
        container.appendChild(attractionName);
    }});
}); 
