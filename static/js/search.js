function submitProteinForm(){
    // Initiate Variables With Form Content
    var protein = $("#search-protein").val();
    var species = $("#search-species").val();
}

$("#protein-form").submit(function(event){
    // cancels the form submission
    event.preventDefault();
    submitProteinForm();
});