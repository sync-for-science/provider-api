function query() {
    var input = $("#provider-input").val();
    $.getJSON("/q", {term: input}, setResults);
}

function setResults(data) {
    console.log(data);
    $("#results").html("<pre>" + JSON.stringify(data, null, 2) + "</pre>");
}

$(function() {
    $("#provider-input").keyup(_.debounce(query, 200));
});
