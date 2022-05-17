
left_image = document.getElementById("left_image");
right_image = document.getElementById("right_image");
click_button = document.getElementById("click_button");

async function output_response(){
    url = "/output_response"
    let res = await fetch(url);
    let data = await res.json();
    right_image.src = data.image;
}
click_button.addEventListener("click", output_response);
