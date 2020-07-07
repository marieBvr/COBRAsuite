$("#protein-form").submit(function(event){
    // cancels the form submission
    event.preventDefault();
    console.log("form");
    submitProteinForm();
});

function submitProteinForm(){
    // Initiate Variables With Form Content
    var protein = $("#search-protein").val();
    var species = $("#search-species").val();
    console.log(protein, species);
 
    // $.ajax({
    //     type: "POST",
    //     url: "php/form-process.php",
    //     data: "name=" + name + "&email=" + email + "&message=" + message,
    //     success : function(text){
    //         if (text == "success"){
    //             formSuccess();
    //         }
    //     }
    // });
}