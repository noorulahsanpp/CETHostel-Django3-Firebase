$(document).ready( function() {

    $("#searchButton").click( function(event) {
        var dept = $("#dept option:selected").text();
        var block = $('#block').find(":selected").text();
        var sem = $('#sem').find(":selected").text();
        alert(block);

        $.ajax({
            type:"GET",
            url:"viewallstudents",
            data:{
                dept:dept,
                sem:sem,
                block:block,
            },
        })
    });
});