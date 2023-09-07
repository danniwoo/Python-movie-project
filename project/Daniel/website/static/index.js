

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

  // card_recommendation_container
  $(document).on("click", "div.card_recommendation_item", function(e){
    console.log(this)
    const search_card_input = $(this).attr('data-Itemname').trim()
    console.log(search_card_input)

    // const search_card_input = card_Itemname
    // console.log(search_card_input)
    if (search_card_input.length > 0) {


      fetch("/search_input", {
        method: "POST",
        body: JSON.stringify({ search_input: search_card_input }),
      }).then((response) => response.text()) // Convert the response to text
        .then((html) => {
          // console.log(html);
          // Replace the entire page content with the new HTML
          document.body.innerHTML = html;
          // document.innerHTML
        })
        .catch((error) => {
          console.error("Error:", error);
        });

        // $.ajax({
        //   url:"/search_input",
        //   type:'POST',
        //   dataType:'json',
        //   data: JSON.stringify({
        //     search_input: search_card_input 
        //   }),
        //   contentType: "text/html; charset=utf-8",
        //   success: function(html){
        //     console.log(html);
        //     // console.log(JSON.parse(response));
        //     document.body.innerHTML = html.text();
        //   },
        //   error: function(xhr, status, error){
        //     console.log(xhr.responseText);
        //   }
        // });   
    }
  });