function add2Cart(){
    // console.log('siuuuu')
    // console.log('siuuuu')
    item_name=$("#item_name").text()
    item_price=$("#item_price").text()
    item_quantity=$("#item_quantity").val()
    console.log( item_name !== null && item_name !== "")
    console.log(item_quantity >= 1 && item_name !== "" && item_price!== "")
    if (item_quantity >= 1 && item_name && item_price){
        console.log(item_name)
        console.log(item_price)
        console.log(item_quantity)

        fetch("/cart", {
            method: "POST",
            body: JSON.stringify({ 
                "Itemname": item_name,
                "Price": item_price,
                "Quantity": item_quantity
            }),
          }).then((response) => response.text()) // Convert the response to text
            .then((resp) => {
              console.log("success:",resp);
                alert(resp);
              // Replace the entire page content with the new HTML
            //   document.body.innerHTML = html;
              // document.innerHTML
            })
            .catch((error) => {
              console.error("Error:", error);
            });

        }
    }




fetch("/cart/count", {
  method: "GET"
}).then((response) => response.text()) // Convert the response to text
  .then((shop_list_count) => {
    console.log("success:",shop_list_count);
    $("#shop_list_count").text(shop_list_count)

    // if (resp=="success"){
    //   console.log("siuuuuuuuuuuuuuuuuuuuuuuuu")
    // }
    // Replace the entire page content with the new HTML
  //   document.body.innerHTML = html;
    // document.innerHTML
  })
  .catch((error) => {
    console.error("Error:", error);
  });